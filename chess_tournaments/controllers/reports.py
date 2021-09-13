from chess_tournaments.models.tournament import Tournament
from chess_tournaments.views.menu import MenuViews
from chess_tournaments.views.reports import Reports


class ReportsController:

    def __init__(self):
        self.menu_view = MenuViews()
        self.reports_view = Reports()

    def all_players_name(self, players):
        """Player report (sorted by last name)

        @param players: list of players
        """
        players = sorted(players, key=lambda x: x.get('last_name'))
        self.reports_view.display_players(players, "by name")

    def all_players_rank(self, players):
        """Player report (sorted by rank)

        @param players: list of players
        """
        players = sorted(players, key=lambda x: x.get('rank'))
        self.reports_view.display_players(players, "by rank")

    def tournament_players(self):
        """Players in a tournament report
        Select tournament to display players

        @return: player list of selected tournament
        """
        user_input, tournaments = self.tournament_select()

        for i in range(len(tournaments)):
            if user_input == str(tournaments[i]['id']):
                return tournaments[i]["players"]

    def all_tournaments(self):
        """All tournaments report"""
        self.reports_view.display_tournaments_report(Tournament.load_tournament_db())

    def tournament_rounds(self):
        """All rounds from a tournament"""
        user_input, tournaments = self.tournament_select()

        self.reports_view.report_header(tournaments[int(user_input) - 1])
        self.reports_view.display_rounds_report(tournaments[int(user_input) - 1]["rounds"])

    def tournament_matches(self):
        """All matches from a tournament"""
        user_input, tournaments = self.tournament_select()

        self.reports_view.report_header(tournaments[int(user_input) - 1])

        rounds = tournaments[int(user_input) - 1]["rounds"]
        round_matches = []
        for i in range(len(rounds)):
            round_matches.append(rounds[i][3])

        matches = []
        for i in range(len(round_matches)):
            for k in range(4):
                matches.append(round_matches[i][k])

        self.reports_view.display_matches_report(matches)

    def tournament_select(self):
        """Load all tournaments for selection

        @return: user selection, list of all tournaments
        """
        tournaments = Tournament.load_tournament_db()
        self.menu_view.select_tournament(tournaments)
        self.menu_view.input_prompt()
        user_input = input()

        if user_input == "back":
            self.back_to_menu()

        else:
            return user_input, tournaments

    @staticmethod
    def back_to_menu():
        from chess_tournaments.controllers.menu import MenuController
        MenuController().main_menu_start()
