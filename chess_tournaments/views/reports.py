from prettytable import PrettyTable


class Reports:

    def __init__(self):
        self.table = PrettyTable()

        self.player_report_field_names = [
            "ID",
            "Last Name",
            "First Name",
            "Gender",
            "Date of birth",
            "Rank"
        ]

        self.tournament_report_field_names = [
            "ID",
            "Name",
            "Location",
            "Description",
            "Start Date",
            "End Date",
            "Time Control",
            "Rounds",
            "Players (ID / Name)",
            "Matches"
        ]

        self.matches_report_field_names = [
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

    def display_players(self, players):
        print("\n- All players -\n")
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

        print(self.table)

    def display_tournaments(self, tournaments):
        print("\n- All tournaments -")
        self.table.clear()
        self.table.field_names = self.tournament_report_field_names
        self.table.align = "l"

        for i in range(len(tournaments)):
            participants = []
            players = tournaments[i]["players"]
            for k in range(len(players)):
                participants.append(
                    str(players[k]["id"]) + " | " +
                    players[k]["last_name"] + ", " + players[k]["first_name"])

            self.table.add_row([
                tournaments[i]["id"],
                tournaments[i]["name"],
                tournaments[i]["location"],
                tournaments[i]["description"],
                tournaments[i]["start_date"],
                tournaments[i]["end_date"],
                tournaments[i]["time_control"],
                str(tournaments[i]["current_round"]) + "/" + str(tournaments[i]["rounds_total"]),
                participants,
                tournaments[i]["matches"]
            ])

        print(self.table)

    def display_matches(self, matches):
        print("\n- Matches -")
        self.table.clear()
        self.table.field_names = self.matches_report_field_names

        for i in range(len(matches)):
            self.table.add_row(matches[i])

        print(self.table)
