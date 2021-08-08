from chess_tournaments.controllers.tournament import TournamentController
from chess_tournaments.models.tournament import Tournament
from chess_tournaments.views.views import MenuViews


class MenuController:

    def __init__(self):
        pass

    @staticmethod
    def main_menu_start():
        MenuViews.main_menu()
        MenuViews.input_prompt()
        user_input = input().lower()

        if user_input == "1":
            pass

        elif user_input == "2":
            MenuController.resume_tournament()

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
