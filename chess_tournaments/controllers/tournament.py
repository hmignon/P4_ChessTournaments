from chess_tournaments.controllers.menu import MenuController
from chess_tournaments.models.round import Round
from chess_tournaments.views.round import RoundViews
from chess_tournaments.views.menu import MenuViews


class TournamentController:
    def __init__(self):
        pass

    @staticmethod
    def start_tournament(tournament):
        players = tournament["players"]
        rounds_total = tournament["total_rounds"]
        current_round = tournament["current_round"]
        table = Round.match_setup()

        if current_round == 1:
            players = TournamentController.first_round(tournament, players, rounds_total, current_round, table)
            current_round += 1
            while current_round <= rounds_total:
                players = TournamentController.next_rounds(tournament, players, rounds_total, current_round, table)
                current_round += 1
        elif current_round > 1:
            while current_round <= rounds_total:
                players = TournamentController.next_rounds(tournament, players, rounds_total, current_round, table)
                current_round += 1

        TournamentController.tournament_end(players)

    @staticmethod
    def first_round(tournament, players, rounds_total, current_round, table):
        top_players, bottom_players = Round.split_players(Round.sort_players_by_rank(players))
        RoundViews.round_header(current_round, tournament)

        for i in range(rounds_total):
            match = Round.set_matches(i+1, top_players[i], bottom_players[i])
            table.add_row(match)
            tournament["matches"].append(match)
            top_players[i], bottom_players[i] = Round.update_opponents(top_players[i], bottom_players[i])
            # save to db
        RoundViews.display_matches(table)

        RoundViews.round_over()
        user_input = input().lower()
        scores_list = []
        if user_input == "ok":
            players = top_players + bottom_players
            players = TournamentController.end_of_round(scores_list, rounds_total, players)
            return players

    @staticmethod
    def end_of_round(scores_list, rounds_total, players):
        for i in range(rounds_total):
            RoundViews.score_options(i + 1)
            response = TournamentController.input_scores()
            scores_list = Round.get_score(response, scores_list)

        players = Round.update_scores(players, scores_list)
        # save to db
        return players

    @staticmethod
    def input_scores():
        RoundViews.score_input_prompt()
        response = input()
        return response

    @staticmethod
    def next_rounds(tournament, players, rounds_total, current_round, table):
        players = Round.sort_players_by_score(players)
        RoundViews.round_header(current_round, tournament)

        available_list = players
        players_added = []
        table.clear_rows()

        k = 0
        while k < rounds_total:
            if available_list[1]["id"] not in available_list[0]["opponents"]:
                available_list, players_added, table = \
                    TournamentController.match_first_option(k, available_list, players_added, table, tournament)
                players = players_added
                # save to db
            elif available_list[1]["id"] in available_list[0]["opponents"]:
                try:
                    available_list, players_added, table = \
                        TournamentController.match_other_option(k, available_list, players_added, table, tournament)
                    players = players_added
                    # save to db
                except IndexError:
                    available_list, players_added, table = \
                        TournamentController.match_first_option(k, available_list, players_added, table, tournament)
                    players = players_added
                    # save to db

            k += 1

        RoundViews.display_matches(table)
        RoundViews.round_over()
        user_input = input().lower()
        scores_list = []
        if user_input == "ok":
            players = TournamentController.end_of_round(scores_list, rounds_total, players)

        return players

    @staticmethod
    def match_first_option(k, available_list, players_added, table, tournament):
        match = Round.set_matches(k + 1, available_list[0], available_list[1])
        table.add_row(match)
        tournament["matches"].append(match)
        available_list[0], available_list[1] = Round.update_opponents(available_list[0], available_list[1])

        available_list, players_added = Round.update_player_lists(
            available_list[0],
            available_list[1],
            available_list,
            players_added
        )

        return available_list, players_added, table

    @staticmethod
    def match_other_option(k, available_list, players_added, table, tournament):
        match = Round.set_matches(k + 1, available_list[0], available_list[2])
        table.add_row(match)
        tournament["matches"].append(match)
        available_list[0], available_list[2] = Round.update_opponents(available_list[0], available_list[2])

        available_list, players_added = Round.update_player_lists(
            available_list[0],
            available_list[2],
            available_list,
            players_added
        )

        return available_list, players_added, table

    @staticmethod
    def tournament_end(players):
        players = Round.sort_players_by_score(players)
        RoundViews.display_results(players)
        MenuViews.back_to_main_menu()
        user_input = input()
        if user_input == "y":
            MenuController.main_menu_start()
        elif user_input == "n":
            TournamentController.tournament_end(players)
        else:
            MenuViews.input_error()
            TournamentController.tournament_end(players)
