from chess_tournaments.controllers.tournament import TournamentController
from chess_tournaments.models.player import Player
from chess_tournaments.models.tournament import Tournament
from chess_tournaments.views.menu import MenuViews


class MenuController:

    def __init__(self):
        pass

    @staticmethod
    def main_menu_start():
        MenuViews.main_menu()
        MenuViews.input_prompt()
        user_input = input().lower()

        if user_input == "1":
            MenuController.new_tournament()

        elif user_input == "2":
            MenuController.resume_tournament()

        elif user_input == "3":
            MenuController.new_player()

        elif user_input == "exit":
            MenuViews.are_you_sure_exit()
            user_input = input().lower()
            if user_input == "y":
                exit()
            elif user_input == "n":
                MenuController.main_menu_start()

        elif user_input == "back":
            MenuController.main_menu_start()

        else:
            MenuViews.input_error()
            MenuController.main_menu_start()

    @staticmethod
    def new_tournament():
        MenuViews.create_tournament()
        tournament_info = []
        options = [
            "name",
            "location",
            "start date (dd/mm/yyyy)",
            "end date (dd/mm/yyyy)",
            "description",
            "amount of players (8 players default)",
            "amount of rounds (4 rounds default)",
        ]

        for item in options:
            MenuViews.input_prompt_text(item)
            user_input = input()
            tournament_info.append(user_input)

        tournament_info = MenuController.input_time_control(tournament_info)
        tour_players = MenuController.choose_players(int(tournament_info[5]))

        MenuViews.review_tournament(tournament_info, tour_players)
        user_input = input().lower()
        if user_input == "y":
            # serialize and save to db
            pass
        elif user_input == "n":
            MenuController.main_menu_start()

    @staticmethod
    def input_time_control(tournament_info):
        MenuViews.time_control_options()
        MenuViews.input_prompt()
        user_input = str(input())
        if user_input == "1":
            tournament_info.append("Bullet")
        elif user_input == "2":
            tournament_info.append("Blitz")
        elif user_input == "3":
            tournament_info.append("Rapid")
        else:
            MenuViews.input_error()

        return tournament_info

    @staticmethod
    def choose_players(players_total):
        players, id_list = Player.load_player_db()
        tour_players = []
        i = 0
        while i < players_total:
            MenuViews.select_players(players, id_list)
            MenuViews.input_prompt()
            user_input = input()

            if int(user_input) in id_list:
                tour_players.append(players[int(user_input) - 1])
                id_list.pop()
                players.remove(players[int(user_input) - 1])
                i += 1

            else:
                MenuViews.input_error()

        return tour_players

    @staticmethod
    def resume_tournament():
        tournament_list, id_list = Tournament.load_tournament_db()
        MenuViews.resume_tournament(tournament_list, id_list)
        user_input = MenuController.choose_tournament()
        if user_input == "back":
            MenuController.main_menu_start()
        for i in range(len(tournament_list)):
            if user_input == str(id_list[i]):
                TournamentController.start_tournament(tournament_list[i])

    @staticmethod
    def choose_tournament():
        MenuViews.input_prompt()
        user_input = input()
        return user_input

    @staticmethod
    def new_player():
        MenuViews.create_new_player()
        player_info = []
        options = [
            "last name",
            "first name",
            "date of birth (dd/mm/yyyy)",
            "gender [M/F/O]",
            "rank"
        ]
        for item in options:
            MenuViews.input_prompt_text(item)
            user_input = input().title()
            player_info.append(user_input)
        MenuViews.review_player(player_info)
        user_input = input().lower()
        if user_input == "y":
            # serialize and save to db
            pass
        elif user_input == "n":
            MenuController.main_menu_start()
