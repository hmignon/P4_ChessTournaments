from chess_tournaments.controllers.tournament import TournamentController
from chess_tournaments.models.player import Player
from chess_tournaments.models.tournament import Tournament
from chess_tournaments.views.menu import MenuViews
from chess_tournaments.views.reports import Reports


class MenuController:

    def __init__(self):
        self.menu_view = MenuViews()
        self.reports_view = Reports()
        self.tour_controller = TournamentController()

    def main_menu_start(self):
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
            pass

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
        self.menu_view.create_tournament()
        tournament_info = []
        options = [
            "name",
            "location",
            "start date (dd/mm/yyyy)",
            "end date (dd/mm/yyyy)",
            "description",
            "amount of players (8 default)",
            "amount of rounds (4 default)",
        ]

        for item in options:
            self.menu_view.input_prompt_text(item)
            user_input = input()
            tournament_info.append(user_input)

        tournament_info = self.input_time_control(tournament_info)
        tour_players = self.choose_players(int(tournament_info[5]))

        self.menu_view.review_tournament(tournament_info, tour_players)
        user_input = input().lower()

        if user_input == "y":
            tournament = Tournament(
                name=tournament_info[0],
                location=tournament_info[1],
                start_date=tournament_info[2],
                end_date=tournament_info[3],
                description=tournament_info[4],
                time_control=tournament_info[7],
                players=tour_players,
                current_round=1
            )
            tournament.save_tournament_db()

        elif user_input == "n":
            self.main_menu_start()

    def input_time_control(self, tournament_info):
        self.menu_view.time_control_options()
        self.menu_view.input_prompt()
        user_input = str(input())
        if user_input == "1":
            tournament_info.append("Bullet")
        elif user_input == "2":
            tournament_info.append("Blitz")
        elif user_input == "3":
            tournament_info.append("Rapid")
        else:
            self.menu_view.input_error()
            self.input_time_control(tournament_info)

        return tournament_info

    def choose_players(self, players_total):
        players, id_list = Player.load_player_db()
        tour_players = []
        for i in range(len(id_list)):
            players[i]["id"] = id_list[i]

        print(players)

        i = 0
        while i < players_total:
            self.menu_view.select_players(players, i+1)
            self.menu_view.input_prompt()
            user_input = input()

            if user_input in id_list:
                index = id_list.index(user_input)
                tour_players.append(players[index])
                id_list.remove(id_list[index])
                players.remove(players[index])
                i += 1

            else:
                self.menu_view.player_already_selected()

        return tour_players

    def resume_tournament(self):
        tournament_list, id_list = Tournament.load_tournament_db()
        for i in range(len(id_list)):
            tournament_list[i]["id"] = id_list[i]

        self.menu_view.select_tournament(tournament_list, id_list)
        user_input = self.choose_tournament()

        if user_input == "back":
            self.main_menu_start()
        for i in range(len(tournament_list)):
            if user_input == str(id_list[i]):
                self.tour_controller.start_tournament(tournament_list[i])

    def choose_tournament(self):
        self.menu_view.input_prompt()
        user_input = input()
        return user_input

    def new_player(self):
        self.menu_view.create_new_player()
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
            user_input = input().title()
            player_info.append(user_input)

        MenuViews.review_player(player_info)
        user_input = input().lower()

        if user_input == "y":
            player = Player(
                last_name=player_info[0],
                first_name=player_info[1],
                birthday=player_info[2],
                gender=player_info[3],
                rank=int(player_info[4])
            )

            player.serialize_player()
            self.menu_view.player_saved()
            self.main_menu_start()

        elif user_input == "n":
            self.main_menu_start()

    def reports_menu(self):
        self.menu_view.reports_menu()
        self.menu_view.input_prompt()
        user_input = input()

        if user_input == "1":
            players, id_list = Player.load_player_db()
            for i in range(len(id_list)):
                players[i]["id"] = id_list[i]
            players = Player.sort_players_name(players)
            self.reports_view.display_players(players)
            self.main_menu_start()

        elif user_input == "2":
            players, id_list = Player.load_player_db()
            for i in range(len(id_list)):
                players[i]["id"] = id_list[i]
            players = Player.sort_players_rank(players)
            self.reports_view.display_players(players)
            self.main_menu_start()

        elif user_input == "3":
            tournaments, id_list = Tournament.load_tournament_db()
            self.menu_view.select_tournament(tournaments, id_list)
            user_input = self.choose_tournament()

            if user_input == "back":
                self.main_menu_start()

            for i in range(len(tournaments)):
                if user_input == str(id_list[i]):
                    self.reports_view.display_players(tournaments[i]["players"])
            self.main_menu_start()

        elif user_input == "4":
            tournaments, id_list = Tournament.load_tournament_db()
            for i in range(len(id_list)):
                tournaments[i]["id"] = id_list[i]
            self.reports_view.display_tournaments(tournaments)
            self.main_menu_start()

        elif user_input == "5":
            tournaments, id_list = Tournament.load_tournament_db()
            for i in range(len(id_list)):
                tournaments[i]["id"] = id_list[i]
            self.menu_view.select_tournament(tournaments, id_list)
            user_input = self.choose_tournament()

        elif user_input == "6":
            tournaments, id_list = Tournament.load_tournament_db()
            for i in range(len(id_list)):
                tournaments[i]["id"] = id_list[i]
            self.menu_view.select_tournament(tournaments, id_list)
            user_input = self.choose_tournament()
            self.reports_view.display_matches(tournaments[int(user_input)-1]["matches"])
            self.main_menu_start()

        elif user_input == "back":
            self.main_menu_start()

        else:
            self.menu_view.input_error()
            self.reports_menu()
