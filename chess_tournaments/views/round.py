# from prettytable import PrettyTable

class RoundViews:
    def __init__(self):
        pass

    @staticmethod
    def round_number(current_round):
        print("\n- ROUND " + str(current_round) + " - ")

    @staticmethod
    def display_match(match_number, player1, player2):
        print("\nMatch " + str(match_number) + " :")
        match = player1["last_name"] + " | " + str(player1["score"]) + " | " + str(player1["rank"]) + \
            "     vs.     " + \
            player2["last_name"] + " | " + str(player2["score"]) + " | " + str(player2["rank"])
        print(match)
        return match

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
