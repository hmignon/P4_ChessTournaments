from chess_tournaments.models.round import Round
from chess_tournaments.views.views import RoundViews


class TournamentController:
    def __init__(self):
        pass

    @staticmethod
    def start_tournament(tournament):
        players = tournament["players"]
        # tournament_info = info
        rounds_total = tournament["total_rounds"]
        current_round = tournament["current_round"]
        if current_round == 1:
            players = TournamentController.first_round(players, rounds_total, current_round)
            current_round += 1
            while current_round <= rounds_total:
                players = TournamentController.next_round(players, rounds_total, current_round)
                current_round += 1
        elif current_round > 1:
            while current_round <= rounds_total:
                players = TournamentController.next_round(players, rounds_total, current_round)
                current_round += 1

        TournamentController.tournament_end(players)

    @staticmethod
    def first_round(players, rounds_total, current_round):
        top_players, bottom_players = Round.split_players(Round.sort_players_by_rank(players))
        RoundViews.round_number(current_round)
        for i in range(rounds_total):
            RoundViews.display_match(i+1, top_players[i], bottom_players[i])
            top_players[i], bottom_players[i] = Round.update_opponents(top_players[i], bottom_players[i])
            # save to db
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
    def next_round(players, rounds_total, current_round):
        players = Round.sort_players_by_score(Round.sort_players_by_rank(players))
        RoundViews.round_number(current_round)
        available_list = players
        players_added = []
        k = 0
        while k < rounds_total:
            if available_list[1]["id"] not in available_list[0]["opponents"]:
                RoundViews.display_match(k+1, available_list[0], available_list[1])
                available_list[0], available_list[1] = Round.update_opponents(available_list[0], available_list[1])
                available_list, players_added = Round.update_player_lists(
                    available_list[0], available_list[1], available_list, players_added
                )
                # save to db

            elif available_list[1]["id"] in available_list[0]["opponents"]:
                try:
                    RoundViews.display_match(k+1, available_list[0], available_list[2])
                    available_list[0], available_list[2] = Round.update_opponents(available_list[0], available_list[2])

                    available_list, players_added = Round.update_player_lists(
                        available_list[0], available_list[2], available_list, players_added
                    )
                    # save to db

                except IndexError:
                    RoundViews.display_match(k + 1, available_list[0], available_list[1])
                    available_list[0], available_list[1] = Round.update_opponents(available_list[0], available_list[1])

                    available_list, players_added = Round.update_player_lists(
                        available_list[0], available_list[1], available_list, players_added
                    )
                    # save to db
            k += 1

        scores_list = []
        players = TournamentController.end_of_round(scores_list, rounds_total, players_added)
        return players

    @staticmethod
    def tournament_end(players):
        players = Round.sort_players_by_score(players)
        RoundViews.display_results(players)
