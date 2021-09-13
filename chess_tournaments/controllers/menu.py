from chess_tournaments.controllers.reports import ReportsController
from chess_tournaments.controllers.tournament import TournamentController
from chess_tournaments.models.player import Player
from chess_tournaments.models.tournament import Tournament
from chess_tournaments.views.menu import MenuViews


class MenuController:

    def __init__(self):
        self.menu_view = MenuViews()
        self.tour_cont = TournamentController()
        self.reports_cont = ReportsController()

    def main_menu_start(self):
        """Main menu selector :
        Redirects to respective submenus"""

        self.menu_view.main_menu()
        self.menu_view.input_prompt()
        user_input = input().lower()

        if user_input == "1":
            self.new_tournament()

        elif user_input == "2":
            self.resume_tournament()

        elif user_input == "3":
            self.new_player()

        elif user_input == "4":
            self.update_player()

        elif user_input == "5":
            self.reports_menu()

        elif user_input == "exit":
            self.menu_view.are_you_sure_exit()
            user_input = input().lower()

            if user_input == "y":
                exit()
            elif user_input == "n":
                self.main_menu_start()

        else:
            self.menu_view.input_error()
            self.main_menu_start()

    def new_tournament(self):
        """Create new tournament, serialize and save to DB"""
        self.menu_view.create_tournament_header()
        tournament_info = []
        options = [
            "name",
            "location",
            "description"
        ]

        for item in options:
            self.menu_view.input_prompt_text(item)
            user_input = input()

            if user_input == "back":
                self.main_menu_start()

            else:
                tournament_info.append(user_input)

        tournament_info.append(self.input_time_control())
        tour_players = self.select_players(8)

        self.menu_view.review_tournament(tournament_info, tour_players)
        user_input = input().lower()

        if user_input == "y":
            tournament = Tournament(
                t_id=0,
                name=tournament_info[0],
                location=tournament_info[1],
                start_date="Not started",
                end_date="TBD",
                description=tournament_info[2],
                time_control=tournament_info[3],
                players=tour_players,
                current_round=1,
                rounds=[]
            )
            tournament.save_tournament_db()
            self.menu_view.tournament_saved()

            self.menu_view.start_tournament_prompt()
            user_input = input()

            if user_input == "y":
                self.tour_cont.start_tournament(tournament)
            elif user_input == "n":
                self.main_menu_start()

        elif user_input == "n":
            self.main_menu_start()

    def input_time_control(self):
        """Select time control for new tournament

        @return: time control (str)
        """
        self.menu_view.time_control_options()
        self.menu_view.input_prompt()
        user_input = input()

        if user_input == "1":
            return "Bullet"
        elif user_input == "2":
            return "Blitz"
        elif user_input == "3":
            return "Rapid"
        elif user_input == "back":
            self.main_menu_start()
        else:
            self.menu_view.input_error()
            self.input_time_control()

    def select_players(self, players_total):
        """Select players for new tournament

        @param players_total: number of players (int)
        @return: list of selected players
        """
        players = Player.load_player_db()
        id_list = []
        for i in range(len(players)):
            id_list.append(players[i]["id"])

        tour_players = []

        i = 0
        while i < players_total:
            self.menu_view.select_players(players, i+1)
            self.menu_view.input_prompt()
            user_input = input()

            if user_input == "back":
                self.main_menu_start()

            elif not user_input.isdigit():
                self.menu_view.input_error()

            elif int(user_input) in id_list:
                index = id_list.index(int(user_input))
                tour_players.append(players[index])
                id_list.remove(id_list[index])
                players.remove(players[index])
                i += 1

            else:
                self.menu_view.player_already_selected()

        return tour_players

    def resume_tournament(self):
        """Select existing tournament to resume"""
        tournament_list = Tournament.load_tournament_db()

        self.menu_view.select_tournament(tournament_list)
        self.menu_view.input_prompt()
        user_input = input()

        if user_input == "back":
            self.main_menu_start()

        for i in range(len(tournament_list)):
            if user_input == str(tournament_list[i]["id"]):
                t = tournament_list[i]
                t = Tournament(
                    t["id"],
                    t["name"],
                    t["location"],
                    t["start_date"],
                    t["end_date"],
                    t["description"],
                    t["time_control"],
                    t["current_round"],
                    t["players"],
                    t["rounds"],
                    t["rounds_total"]
                )
                self.tour_cont.start_tournament(t)

    def new_player(self):
        """Create new player, serialize and save to DB"""
        self.menu_view.create_new_player_header()
        player_info = []
        options = [
            "last name",
            "first name",
            "date of birth (dd/mm/yyyy)",
            "gender [M/F/O]",
            "rank"
        ]
        for item in options:
            self.menu_view.input_prompt_text(item)
            user_input = input()
            if user_input == "back":
                self.main_menu_start()
            else:
                player_info.append(user_input)

        MenuViews.review_player(player_info)
        user_input = input().lower()

        if user_input == "y":
            player = Player(
                p_id=0,
                last_name=player_info[0],
                first_name=player_info[1],
                birthday=player_info[2],
                gender=player_info[3],
                rank=int(player_info[4])
            )

            player.save_player_db()
            self.menu_view.player_saved()
            self.main_menu_start()

        elif user_input == "n":
            self.main_menu_start()

    def update_player(self):
        """Update existing player info"""
        players = Player.load_player_db()

        self.menu_view.select_players(players, "to update")
        self.menu_view.input_prompt()
        user_input = input()

        if user_input == "back":
            self.main_menu_start()

        p = players[int(user_input) - 1]
        p = Player(
            p['id'],
            p['last_name'],
            p['first_name'],
            p['date_of_birth'],
            p['gender'],
            p['rank']
        )

        options = [
            "last name",
            "first name",
            "date of birth",
            "gender",
            "rank"
        ]
        self.menu_view.update_player_info(p, options)
        self.menu_view.input_prompt()
        user_input = input()

        if user_input == "back":
            self.main_menu_start()

        elif int(user_input) <= len(options):
            updated_info = (options[int(user_input) - 1]).replace(" ", "_")
            self.menu_view.input_prompt_text(
                f"new {options[int(user_input) - 1]}")
            user_input = input()

            if user_input == "back":
                self.main_menu_start()

            else:
                p.update_player_db(user_input, updated_info)
                self.menu_view.player_saved()

                self.update_player()

        else:
            self.menu_view.input_error()
            self.update_player()

    def reports_menu(self):
        """Reports menu selector"""
        self.menu_view.reports_menu()
        self.menu_view.input_prompt()
        user_input = input()

        if user_input == "1":
            self.player_reports_sorting(Player.load_player_db())

        elif user_input == "2":
            self.player_reports_sorting(self.reports_cont.tournament_players())

        elif user_input == "3":
            self.reports_cont.all_tournaments()

        elif user_input == "4":
            self.reports_cont.tournament_rounds()

        elif user_input == "5":
            self.reports_cont.tournament_matches()

        elif user_input == "back":
            self.main_menu_start()

        else:
            self.menu_view.input_error()
            self.reports_menu()

        self.menu_view.other_report()
        user_input = input()

        if user_input == "y":
            self.reports_menu()

        elif user_input == "n":
            self.main_menu_start()

    def player_reports_sorting(self, players):
        """Select sorting option (name or rank) for players

        @param players: list of players
        """
        self.menu_view.reports_player_sorting()
        self.menu_view.input_prompt()
        user_input = input()

        if user_input == "1":
            self.reports_cont.all_players_name(players)

        elif user_input == "2":
            self.reports_cont.all_players_rank(players)

        elif user_input == "back":
            self.main_menu_start()
