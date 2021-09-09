from prettytable import PrettyTable


class RoundViews:

    def __init__(self):
        self.table = PrettyTable()

        self.round_field_names = [
            "Match #",
            "Name P1",
            "Rank P1",
            "Score P1",
            " ",
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
        """Display matches for current round as table

        @param matches: list of matches tuples
        """
        self.table.clear()
        self.table.field_names = self.round_field_names

        for i in range(len(matches)):
            row = list(matches[i])
            row.insert(0, str(i+1))
            row.insert(4, "vs.")

            self.table.add_row(row)

        print(self.table)

    def display_results(self, t):
        """Display results at the end of the tournament

        @param t: current tournament
        """
        self.table.clear()
        self.table.field_names = self.results_field_names

        for i in range(len(t.players)):
            self.table.add_row([
                i+1,
                t.players[i]["last_name"] + ", " + t.players[i]["first_name"],
                t.players[i]["score"],
                t.players[i]["rank"]
            ])

        print("\n\n- FINAL SCORES -\n")
        print(f"{t.name.upper()}, {t.location.title()} | Description : {t.description}")
        print(f"Start : {t.start_date} | End : {t.end_date} | Time control : {t.time_control}\n")

        print(self.table)

    @staticmethod
    def round_header(t, start_time):
        """Display tournament info as a round header

        @param t: current tournament
        @param start_time: tournament start time (str)
        """
        print("\n\n")

        h_1 = f"{t.name.upper()}, {t.location.title()} | Description : {t.description}"
        h_2 = f"Start date and time : {t.start_date} | Time control : {t.time_control}\n"
        h_3 = f"- ROUND {t.current_round}/{t.rounds_total} | {start_time} -"

        print(h_1.center(100, " "))
        print(h_2.center(100, " "))
        print(h_3.center(100, " "))

    @staticmethod
    def round_over():
        print("\nRound over ? [ok]")
        print("Back to main menu ? [back]")

    @staticmethod
    def score_options(match_number):
        print("\nMatch ", match_number)
        print('[0] Draw')
        print('[1] Player 1 wins')
        print('[2] Player 2 wins')
        print("\n[back] Back to main menu")

    @staticmethod
    def score_input_prompt():
        print('\nEnter result :', end=' ')
