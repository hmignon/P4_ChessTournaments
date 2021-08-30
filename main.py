from chess_tournaments.controllers.menu import MenuController
from chess_tournaments.views.menu import MenuViews


def main():
    MenuViews.app_title()
    MenuController().main_menu_start()


if __name__ == "__main__":
    main()
