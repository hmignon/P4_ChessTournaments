from chess_tournaments.models.round import Round
from chess_tournaments.models.tournament import Tournament
from chess_tournaments.views.round import RoundViews
from chess_tournaments.views.menu import MenuViews


class TournamentController:
    def __init__(self):
        self.menu_view = MenuViews()
        self.round_view = RoundViews()
        self.round = Round()

    def start_tournament(self, tournament):
        players = tournament["players"]
        rounds_total = tournament["rounds_total"]
        current_round = tournament["current_round"]

        if current_round == 1:
            players, tournament = self.first_round(tournament, players, rounds_total, current_round)
            current_round += 1
            Tournament.update_tournament_db(
                int(tournament["id"]),
                tournament["matches"],
                players,
                int(current_round)
            )

            while current_round <= rounds_total:
                players, tournament = self.next_rounds(tournament, players, rounds_total, current_round)
                current_round += 1
                Tournament.update_tournament_db(
                    int(tournament["id"]),
                    tournament["matches"],
                    players,
                    int(current_round)
                )

        elif current_round > 1:
            while current_round <= rounds_total:
                players, tournament = self.next_rounds(tournament, players, rounds_total, current_round)
                current_round += 1
                Tournament.update_tournament_db(
                    int(tournament["id"]),
                    tournament["matches"],
                    players,
                    int(current_round)
                )

        self.tournament_end(players)

    def first_round(self, tournament, players, rounds_total, current_round):
        top_players, bottom_players = self.round.split_players(self.round.sort_players_by_rank(players))
        self.round_view.round_header(current_round, tournament)

        for i in range(rounds_total):
            match = self.round.set_matches(top_players[i], bottom_players[i])
            tournament["matches"].append(match)
            top_players[i], bottom_players[i] = self.round.update_opponents(top_players[i], bottom_players[i])

        self.round_view.display_matches(tournament["matches"])

        self.round_view.round_over()
        user_input = input().lower()
        scores_list = []

        if user_input == "ok":
            players = top_players + bottom_players
            players = self.end_of_round(scores_list, rounds_total, players)

            return players, tournament

    def end_of_round(self, scores_list, rounds_total, players):
        for i in range(rounds_total):
            self.round_view.score_options(i + 1)
            response = self.input_scores()
            scores_list = self.round.get_score(response, scores_list)

        players = self.round.update_scores(players, scores_list)

        return players

    def input_scores(self):
        self.round_view.score_input_prompt()
        response = input()
        return response

    def next_rounds(self, tournament, players, rounds_total, current_round):
        players = self.round.sort_players_by_score(players)
        self.round_view.round_header(current_round, tournament)

        available_list = players
        players_added = []

        k = 0
        while k < rounds_total:
            if available_list[1]["id"] not in available_list[0]["opponents"]:
                available_list, players_added, tournament = \
                    self.match_first_option(available_list, players_added, tournament)
                players = players_added

            elif available_list[1]["id"] in available_list[0]["opponents"]:
                try:
                    available_list, players_added, tournament = \
                        self.match_other_option(available_list, players_added, tournament)
                    players = players_added

                except IndexError:
                    available_list, players_added, tournament = \
                        self.match_first_option(available_list, players_added, tournament)
                    players = players_added

            k += 1

        self.round_view.display_matches(tournament["matches"])
        self.round_view.round_over()
        user_input = input().lower()
        scores_list = []
        if user_input == "ok":
            players = self.end_of_round(scores_list, rounds_total, players)

        return players, tournament

    def match_first_option(self, available_list, players_added, tournament):
        match = self.round.set_matches(available_list[0], available_list[1])
        tournament["matches"].append(match)
        available_list[0], available_list[1] = self.round.update_opponents(available_list[0], available_list[1])

        available_list, players_added = self.round.update_player_lists(
            available_list[0],
            available_list[1],
            available_list,
            players_added
        )

        return available_list, players_added, tournament

    def match_other_option(self, available_list, players_added, tournament):
        match = self.round.set_matches(available_list[0], available_list[2])
        tournament["matches"].append(match)
        available_list[0], available_list[2] = self.round.update_opponents(available_list[0], available_list[2])

        available_list, players_added = self.round.update_player_lists(
            available_list[0],
            available_list[2],
            available_list,
            players_added
        )

        return available_list, players_added, tournament

    def tournament_end(self, players):
        players = self.round.sort_players_by_score(self.round.sort_players_by_rank(players))
        self.round_view.display_results(players)

        self.menu_view.back_to_main_menu()
        user_input = input()
        if user_input == "y":
            pass
        elif user_input == "n":
            self.tournament_end(players)
        else:
            self.menu_view.input_error()
            self.tournament_end(players)
