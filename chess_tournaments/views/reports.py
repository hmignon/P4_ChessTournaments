from prettytable import PrettyTable


class Reports:

    def __init__(self):
        pass

    @staticmethod
    def display_players(players):
        print("\n- All players -\n")
        table = PrettyTable()
        table.field_names = ["ID", "Last Name", "First Name", "Gender", "Date of birth", "Rank"]

        for i in range(len(players)):
            table.add_row([
                players[i]["id"],
                players[i]["last_name"],
                players[i]["first_name"],
                players[i]["gender"],
                players[i]["date_of_birth"],
                players[i]["rank"]
            ])

        print(table)
