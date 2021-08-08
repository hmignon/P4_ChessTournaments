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
        # print("[1] Create new tournament")
        print("[2] Resume tournament")
        # print("[3] Edit tournament")
        # print("[4] Create new player")
        # print("[5] Edit existing player")
        # print("[6] Reports")
        print("\n[exit] Exit program")

    @staticmethod
    def create_tournament():
        print("\n" * 3 + "- NEW TOURNAMENT -\n")
        # input name, location, start date, end date, players, and description
        print("\n[back] Back to main menu")

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
    def input_prompt():
        print("\nType number option and press enter : ", end='')

    @staticmethod
    def are_you_sure_exit():
        print("Are you sure you want to exit the program ? [y/n] ", end='')

    @staticmethod
    def input_error():
        print("Input error, please enter a valid option.")


class RoundViews:
    def __init__(self):
        pass

    @staticmethod
    def round_number(current_round):
        print("\n- ROUND " + str(current_round) + " - ")

    @staticmethod
    def display_match(match_number, player1, player2):
        print("\nMatch " + str(match_number) + " :")
        print(
            player1["last_name"] + " | " + str(player1["score"]) + " | " + str(player1["rank"])
            + "    vs.    " +
            player2["last_name"] + " | " + str(player2["score"]) + " | " + str(player2["rank"])
        )

    @staticmethod
    def round_over():
        print("\nRound over ? [ok]", end=' ')

    @staticmethod
    def score_options(match_number):
        print("\nMatch ", match_number)
        print('[0] Draw')
        print('[1] Player 1 wins')
        print('[2] Player 2 wins')

    @staticmethod
    def score_input_prompt():
        print('\nWho won ?', end=' ')

    @staticmethod
    def display_results(players):
        print("\n\n- FINAL SCORES -\n")
        for i in range(len(players)):
            print(players[i]['last_name'], "=", end=' ')
            print(str(players[i]['score']) + " pts")
