from datetime import datetime

from chess_tournaments.controllers.database import DatabaseController
from chess_tournaments.models.round import Round
from chess_tournaments.views.round import RoundViews
from chess_tournaments.views.menu import MenuViews


class TournamentController:

    def __init__(self):
        self.menu_view = MenuViews()
        self.round_view = RoundViews()
        self.db = DatabaseController()

        self.timer = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def start_tournament(self, tournament):
        """Tournament main structure
        Start from first round or resume tournament according to round number
        Set start and end timers and save to DB"""
        rounds_total = tournament.rounds_total
        current_round = tournament.current_round

        if current_round == 1:
            self.db.update_timer(tournament.t_id, self.timer, 'start_date')

            players, tournament = self.first_round(tournament, rounds_total, current_round)
            current_round += 1
            self.db.update_tournament_db(
                int(tournament.t_id),
                tournament.rounds,
                players,
                int(current_round)
            )

            while current_round <= rounds_total:
                players, tournament = self.next_rounds(tournament, rounds_total, current_round)
                current_round += 1
                self.db.update_tournament_db(
                    int(tournament.t_id),
                    tournament.rounds,
                    players,
                    int(current_round)
                )

        elif current_round > 1:
            while current_round <= rounds_total:
                players, tournament = self.next_rounds(tournament, rounds_total, current_round)
                current_round += 1
                self.db.update_tournament_db(
                    int(tournament.t_id),
                    tournament.rounds,
                    players,
                    int(current_round)
                )

        self.db.update_timer(tournament.t_id, self.timer, 'end_date')

        self.tournament_end(tournament)

    def first_round(self, tournament, rounds_total, current_round):
        """First round : top players vs. bottom players
        Get pairings and set round to save to DB"""
        r = Round("Round 1", self.timer, "TBD")
        tournament.sort_players_by_rank()
        top_players, bottom_players = tournament.split_players()
        self.round_view.round_header(current_round, tournament.serialize_tournament(), r.start_datetime)

        for i in range(rounds_total):
            r.get_match_pairing(top_players[i], bottom_players[i])
            top_players[i], bottom_players[i] = self.update_opponents(top_players[i], bottom_players[i])

        self.round_view.display_matches(r.matches)

        self.round_view.round_over()
        user_input = input().lower()
        scores_list = []

        if user_input == "ok":
            r.end_datetime = self.timer
            tournament.rounds.append(r.set_round())

            players = top_players + bottom_players
            players = self.end_of_round(scores_list, rounds_total, players)

            return players, tournament

    def next_rounds(self, tournament, rounds_total, current_round):
        """Next rounds : set possible pairings
        Get pairings and set round to save to DB"""
        r = Round(("Round " + str(current_round)), self.timer, "TBD")
        players = tournament.sort_players_by_score()
        self.round_view.round_header(current_round, tournament.serialize_tournament(), r.start_datetime)

        available_list = tournament.sort_players_by_score()
        players_added = []

        k = 0
        while k < rounds_total:
            if available_list[1]["id"] in available_list[0]["opponents"]:
                try:
                    available_list, players_added, tournament = \
                        self.match_other_option(available_list, players_added, tournament, r)
                    players = players_added

                except IndexError:
                    available_list, players_added, tournament = \
                        self.match_first_option(available_list, players_added, tournament, r)
                    players = players_added

            elif available_list[1]["id"] not in available_list[0]["opponents"]:
                available_list, players_added, tournament = \
                    self.match_first_option(available_list, players_added, tournament, r)
                players = players_added

            k += 1

        self.round_view.display_matches(r.matches)

        self.round_view.round_over()
        user_input = input().lower()
        scores_list = []

        if user_input == "ok":
            r.end_datetime = self.timer
            tournament.rounds.append(r.set_round())
            players = self.end_of_round(scores_list, rounds_total, players)

        return players, tournament

    def match_first_option(self, available_list, players_added, tournament, r):
        """Main pairing option

        @param available_list: list of players not set in match for current round
        @param players_added: list of players already in match for current round
        @param tournament: current tournament dict
        @param r: current round
        @return: updated lists and tournament
        """
        r.get_match_pairing(available_list[0], available_list[1])
        available_list[0], available_list[1] = self.update_opponents(available_list[0], available_list[1])

        available_list, players_added = self.update_player_lists(
            available_list[0],
            available_list[1],
            available_list,
            players_added
        )

        return available_list, players_added, tournament

    def match_other_option(self, available_list, players_added, tournament, r):
        """Alternative pairing option

        @param available_list: list of players not set in match for current round
        @param players_added: list of players already in match for current round
        @param tournament: current tournament dict
        @param r: current round
        @return: updated lists and tournament
        """
        r.get_match_pairing(available_list[0], available_list[2])
        available_list[0], available_list[2] = self.update_opponents(available_list[0], available_list[2])

        available_list, players_added = self.update_player_lists(
            available_list[0],
            available_list[2],
            available_list,
            players_added
        )

        return available_list, players_added, tournament

    def end_of_round(self, scores_list, rounds_total, players):
        """End of round : update player scores

        @param scores_list: list of scores
        @param rounds_total: total number of rounds (int)
        @param players: players list
        @return: players list with updated scores
        """
        for i in range(rounds_total):
            self.round_view.score_options(i + 1)
            response = self.input_scores()
            scores_list = self.get_score(response, scores_list)

        players = self.update_scores(players, scores_list)

        return players

    def input_scores(self):
        """Score input"""
        self.round_view.score_input_prompt()
        response = input()
        return response

    @staticmethod
    def update_player_lists(player_1, player_2, available_list, players_added):
        """Update player lists :
        Add unavailable player to respective list
        Remove available player form respective list

        @param player_1: player 1 (dict)
        @param player_2: player 2 (dict)
        @param available_list: list of players not set in match for current round
        @param players_added: list of players already in match for current round
        @return: list of available players, list of unavailable players
        """
        players_added.extend([player_1, player_2])
        available_list.remove(player_1)
        available_list.remove(player_2)

        return available_list, players_added

    @staticmethod
    def get_score(response, scores_list):
        """Input scores for each match in current round

        @param response: user input (int)
        @param scores_list: list of scores
        @return: updated list of scores
        """
        if response == "0":
            scores_list.extend([0.5, 0.5])
        elif response == "1":
            scores_list.extend([1.0, 0.0])
        elif response == "2":
            scores_list.extend([0.0, 1.0])

        return scores_list

    @staticmethod
    def update_scores(players, scores_list):
        """Update player scores

        @param players: list of players
        @param scores_list: list of scores
        @return: list of players with updated scores
        """
        for i in range(len(players)):
            players[i]["score"] += scores_list[i]

        return players

    @staticmethod
    def update_opponents(player_1, player_2):
        player_1["opponents"].append(player_2["id"])
        player_2["opponents"].append(player_1["id"])

        return player_1, player_2

    def tournament_end(self, tournament):
        """End of tournament : display final results
        Offer user to update ranks

        @param tournament: current tournament dict
        """
        tournament.sort_players_by_rank()
        players = tournament.sort_players_by_score()

        self.round_view.display_results(players, tournament.serialize_tournament())

        self.menu_view.update_rank()
        user_input = input()

        if user_input == "y":
            for i in range(len(players)):
                self.update_ranks(players)

        elif user_input == "n":
            pass

    def update_ranks(self, players):
        """Update player ranks and save to DB

        @param players: list of players
        """
        self.menu_view.select_players(players, "")
        self.menu_view.input_prompt()
        user_input = input()

        player = players[int(user_input) - 1]
        self.menu_view.update_player_info(player, ["rank"])
        self.menu_view.input_prompt()
        user_input = int(input())

        self.db.update_player_db(player, user_input, "rank")
