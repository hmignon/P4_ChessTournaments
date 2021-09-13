from prettytable import PrettyTable


class Reports:

    def __init__(self):

        self.table = PrettyTable()

        self.player_report_field_names = [
            "ID",
            "Last name",
            "First name",
            "Gender",
            "Date of birth",
            "Rank"
        ]

        self.tournament_report_field_names = [
            "ID",
            "Name",
            "Location",
            "Description",
            "Start date",
            "End date",
            "Time control",
            "Last round played",
            "Players (ID : Name)",
        ]

        self.matches_report_field_names = [
            "Name P1",
            "Rank P1",
            "Score P1",
            " ",
            "Name P2",
            "Rank P2",
            "Score P2"
        ]

        self.rounds_report_field_names = [
            "Round #",
            "Started at",
            "Ended at",
            "Matches"
        ]

    def display_players(self, players, sorting):
        """Display player report (all sorting types)"""
        self.table.clear()
        self.table.field_names = self.player_report_field_names
        self.table.align = "l"

        for i in range(len(players)):
            self.table.add_row([
                players[i]["id"],
                players[i]["last_name"],
                players[i]["first_name"],
                players[i]["gender"],
                players[i]["date_of_birth"],
                players[i]["rank"]
            ])

        print(f"\n\n\n- All players ({sorting}) -\n")
        print(self.table)

    def display_tournaments_report(self, tournaments):
        """Display tournament reports"""
        self.table.clear()
        self.table.field_names = self.tournament_report_field_names
        self.table.align = "l"

        for i in range(len(tournaments)):
            participants = []
            players = tournaments[i]["players"]
            for k in range(len(players)):
                participants.append(
                    str(players[k]["id"]) + " : " + players[k]["last_name"])

            self.table.add_row([
                tournaments[i]["id"],
                tournaments[i]["name"],
                tournaments[i]["location"],
                tournaments[i]["description"],
                tournaments[i]["start_date"],
                tournaments[i]["end_date"],
                tournaments[i]["time_control"],
                str(tournaments[i]["current_round"]-1) + "/" + str(tournaments[i]["rounds_total"]),
                participants
            ])

        print("\n\n\n- All tournaments -\n")
        print(self.table)

    def display_matches_report(self, matches):
        """Display matches in tournament report"""
        self.table.clear()
        self.table.field_names = self.matches_report_field_names
        self.table.align = "l"

        for i in range(len(matches)):
            matches[i].insert(3, "vs.")
            self.table.add_row(matches[i])

        print(f"\n\n- All played matches ({len(matches)} total) -\n")
        print(self.table)

    def display_rounds_report(self, rounds):
        """Display rounds in tournament report"""
        self.table.clear()
        self.table.field_names = self.rounds_report_field_names
        self.table.align = "l"

        for i in range(len(rounds)):
            for j in range(4):
                if j == 0:
                    self.table.add_row([
                        rounds[i][0],
                        rounds[i][1],
                        rounds[i][2],
                        rounds[i][3][j]
                    ])
                else:
                    self.table.add_row([
                        ' ',
                        ' ',
                        ' ',
                        rounds[i][3][j]
                    ])

        print("\n\n- All played rounds -\n")
        print(self.table)

    @staticmethod
    def report_header(info):
        """Header for tournament reports

        @param info: tournament (dict)
        """
        print("\n\n")

        h_1 = f"{info['name'].upper()}, {info['location'].title()} | Description : {info['description']}"
        h_2 = \
            f"Start date : {info['start_date']} | " \
            f"End date : {info['end_date']} | " \
            f"Time control : {info['time_control']} | " \
            f"Rounds played : {info['current_round']-1}/{info['rounds_total']}"

        print(h_1)
        print(h_2)
