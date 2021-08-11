class RoundViews:

    def __init__(self):
        pass

    @staticmethod
    def round_header(current_round, info):
        print(f"\n\n{info['name'].upper()}, {info['location'].title()}", end=' | ')
        print(f"Description : {info['description']}")
        print(f"Start date : {info['start_date']}", end=' | ')
        print(f"End date : {info['end_date']}", end=' | ')
        print(f"Time control : {info['time_control']}")

        print(f"\n- ROUND {current_round}/{info['total_rounds']} - ")

    @staticmethod
    def display_matches(table):
        print(table)

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
