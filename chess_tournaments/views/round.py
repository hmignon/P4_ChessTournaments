from prettytable import PrettyTable


class RoundViews:

    def __init__(self):
        self.table = PrettyTable()

        self.match_field_names = [
            "ID P1",
            "Name P1",
            "Rank P1",
            "Score P1",
            " ",
            "ID P2",
            "Name P2",
            "Rank P2",
            "Score P2"
        ]

        self.results_field_names = [
            "Tournament ranking",
            "Name",
            "Final Score",
            "Global ranking"
        ]

    def display_matches(self, matches):
        self.table.clear()
        self.table.field_names = self.match_field_names

        i = -4
        while i != 0:
            self.table.add_row(matches[i])
            i += 1

        print(self.table)

    def display_results(self, players):
        print("\n\n- FINAL SCORES -\n")
        self.table.field_names = self.results_field_names
        self.table.clear_rows()

        for i in range(len(players)):
            self.table.add_row([
                i+1,
                players[i]["last_name"] + ", " + players[i]["first_name"],
                players[i]["score"],
                players[i]["rank"]
            ])

        print(self.table)

    @staticmethod
    def round_header(current_round, info):
        print(f"\n\n{info['name'].upper()}, {info['location'].title()}", end=' | ')
        print(f"Description : {info['description']}")
        print(f"Start date : {info['start_date']}", end=' | ')
        print(f"End date : {info['end_date']}", end=' | ')
        print(f"Time control : {info['time_control']}")

        print(f"\n- ROUND {current_round}/{info['rounds_total']} - ")

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
        print('\nEnter result :', end=' ')
