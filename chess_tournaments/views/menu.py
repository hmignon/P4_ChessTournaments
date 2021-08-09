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
        # print("[5] Reports")
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
        print("\n\nNew tournament created : ", end='')
        print(info[0] + " at " + info[1], end=' | ')
        print("Description : " + info[4], end=' | ')
        print("Start date : " + info[2], end=' | ')
        print("End date : " + info[3], end=' | ')
        print("Rounds : " + info[6], end=' | ')
        print("Time control : " + info[7], end=' | ')
        print(f"Players ({info[5]} total) : ", end='')
        for item in players:
            print(item)
        print("\nSave to database ? [y/n] ", end='')

    @staticmethod
    def select_players(players, id_list):
        print("\nSelect players :")
        for i in range(len(players)):
            print("[" + str(id_list[i]) + "]", end=' ')
            print(players[i]["last_name"] + ", " + players[i]["first_name"], end=" | ")
            print(players[i]["date_of_birth"], end=" | ")
            print("Rank : " + str(players[i]["rank"]))

    @staticmethod
    def resume_tournament(tournament_list, id_list):
        print("\n" * 3 + "- RESUME TOURNAMENT -\n")

        for i in range(len(tournament_list)):
            print("[" + str(id_list[i]) + "]", end=' ')
            print(tournament_list[i]["name"], end=' | ')
            print(tournament_list[i]["location"], end=" | ")
            print(tournament_list[i]["description"], end=' | ')
            print("Started on : " + tournament_list[i]["start_date"])

        print("\n[back] Back to main menu")

    @staticmethod
    def create_new_player():
        print("\n" * 3 + "- NEW PLAYER -\n")

    @staticmethod
    def review_player(info):
        print("\n\nNew player created : ", end='')
        print(info[0] + ", " + info[1], end=' | ')
        print("Date of birth : " + info[2], end=' | ')
        print("Gender : " + info[3], end=' | ')
        print("Rank : " + info[4])
        print("\nSave to database ? [y/n] ", end='')

    @staticmethod
    def input_prompt_text(option):
        print(f"\nEnter {option} : ", end='')

    @staticmethod
    def input_prompt():
        print("\nType number option and press enter : ", end='')

    @staticmethod
    def are_you_sure_exit():
        print("Are you sure you want to exit the program ? [y/n] ", end='')

    @staticmethod
    def input_error():
        print("Input error, please enter a valid option.")
