class MenuViews:

    def __init__(self):
        pass

    @staticmethod
    def app_title():
        print("\n\n----------------------------------")
        print("        CHESS TOURNAMENTS")
        print("----------------------------------")

    @staticmethod
    def main_menu():
        print("\n" * 3 + "- MAIN MENU -\n")
        print("[1] Create new tournament")
        print("[2] Resume tournament")
        print("[3] Create new player")
        # print("[4] Edit existing player")
        print("[5] Reports")
        print("\n[exit] Exit program")

    @staticmethod
    def create_tournament():
        print("\n" * 3 + "- NEW TOURNAMENT -\n")

    @staticmethod
    def time_control_options():
        print("\nSelect time control :")
        print("[1] Bullet")
        print("[2] Blitz")
        print("[3] Rapid")

    @staticmethod
    def review_tournament(info, players):
        print("\n\n- New tournament created -\n")
        print(f"{info[0].upper()}, {info[1].title()}", end=' | ')
        print(f"Description : {info[4]}", end=' | ')
        print(f"Start date : {info[2]}", end=' | ')
        print(f"End date : {info[3]}", end=' | ')
        print(f"Rounds : {info[6]}", end=' | ')
        print(f"Time control : {info[7]}")
        print(f"\nPlayers ({info[5]} total) :\n")

        for item in players:
            print(f"Player {item['id']} : ", end='')
            print(f"{item['last_name']}, {item['first_name']}", end=' | ')
            print(f"{item['date_of_birth']}", end=' | ')
            print(f"Rank : {item['rank']}")

        print("\nSave to database ? [y/n] ", end='')

    @staticmethod
    def select_players(players, player_number):
        print(f"\nSelect Player {player_number} :")
        for i in range(len(players)):
            print(f"[{players[i]['id']}]", end=' ')
            print(f"{players[i]['last_name']}, {players[i]['first_name']}", end=" | ")
            print(f"{players[i]['date_of_birth']}", end=" | ")
            print(f"Rank : {players[i]['rank']}")

    @staticmethod
    def resume_tournament(tournament_list, id_list):
        print("\n" * 3 + "- RESUME TOURNAMENT -\n")

        for i in range(len(tournament_list)):
            print(f"[{id_list[i]}]", end=' ')
            print(tournament_list[i]['name'], end=' | ')
            print(tournament_list[i]['location'], end=" | ")
            print(tournament_list[i]['description'], end=' | ')
            print(f"Started on : {tournament_list[i]['start_date']}")

        print("\n[back] Back to main menu")

    @staticmethod
    def create_new_player():
        print("\n" * 3 + "- NEW PLAYER -\n")

    @staticmethod
    def review_player(info):
        print("\n\n- New player created -\n")
        print(f"{info[0]}, {info[1]}", end=' | ')
        print(f"Date of birth : {info[2]}", end=' | ')
        print(f"Gender : {info[3]}", end=' | ')
        print(f"Rank : {info[4]}")
        print("\nSave to database ? [y/n] ", end='')

    @staticmethod
    def player_saved():
        print("\nPlayer successfully saved to database !")

    @staticmethod
    def reports_menu():
        print("\n" * 3 + "- REPORTS -\n")
        print("[1] All players (by name)")
        print("[2] All players (by rank)")
        print("[3] Players in a tournament")
        print("[4] All tournaments")
        print("[5] Rounds in a tournament")
        print("[6] Matches in a tournament")
        print("\n[back] Back to main menu")

    @staticmethod
    def input_prompt_text(option):
        print(f"\nEnter {option} : ", end='')

    @staticmethod
    def input_prompt():
        print("\nType number option and press Enter : ", end='')

    @staticmethod
    def back_to_main_menu():
        print("Back to main menu ? [y/n] ", end='')

    @staticmethod
    def are_you_sure_exit():
        print("Are you sure you want to exit the program ? [y/n] ", end='')

    @staticmethod
    def input_error():
        print("\nInput error, please enter a valid option.")

    @staticmethod
    def player_already_selected():
        print("\nPlayer already selected. Please select other player.")
