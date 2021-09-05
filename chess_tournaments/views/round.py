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

    def display_results(self, players, tournament):
        """Display results at the end of the tournament

        @param players: list of players dicts
        @param tournament: tournament dict
        """
        print("\n\n- FINAL SCORES -\n")
        print(f"{tournament['name']} | Start : {tournament['start_date']} | End : {tournament['end_date']}\n")
        self.table.clear()
        self.table.field_names = self.results_field_names

        for i in range(len(players)):
            self.table.add_row([
                i+1,
                players[i]["last_name"] + ", " + players[i]["first_name"],
                players[i]["score"],
                players[i]["rank"]
            ])

        print(self.table)

    @staticmethod
    def round_header(current_round, info, start_time):
        """Display tournament info as a round header

        @param current_round: current round number (int)
        @param info: tournament info (dict)
        @param start_time: tournament start time (str)
        """
        print("\n\n")

        h_1 = f"{info['name'].upper()}, {info['location'].title()} | Description : {info['description']}"
        h_2 = f"Start date and time : {info['start_date']} | Time control : {info['time_control']}\n"
        h_3 = f"- ROUND {current_round}/{info['rounds_total']} | {start_time} -"

        print(h_1.center(100, " "))
        print(h_2.center(100, " "))
        print(h_3.center(100, " "))

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
