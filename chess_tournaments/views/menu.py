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
        print("\n\n=== MAIN MENU ===\n")
        print("[1] Create new tournament")
        print("[2] Resume tournament")
        print("[3] Create new player")
        print("[4] Edit existing player")
        print("[5] Reports")
        print("\n[exit] Exit program")

    @staticmethod
    def create_tournament_header():
        print("\n" * 3 + "--- NEW TOURNAMENT ---")

    @staticmethod
    def time_control_options():
        print("\nSelect time control :")
        print("[1] Bullet")
        print("[2] Blitz")
        print("[3] Rapid")
        print("\n[back] Back to main menu")

    @staticmethod
    def review_tournament(info, players):
        """Display all input info to review before saving to database

        @param info: input info list
        @param players: list of selected players
        """
        print("\n\nNew tournament created :\n")
        print(f"{info[0].upper()}, {info[1].title()}", end=' | ')
        print(f"Description : {info[2]}", end=' | ')
        print("Rounds : 4", end=' | ')
        print(f"Time control : {info[3]}")
        print("\nPlayers (8 total) :\n")

        for item in players:
            print(f"Player {players.index(item) + 1} : ", end='')
            print(f"{item['id']}", end=' | ')
            print(f"{item['last_name']}, {item['first_name']}", end=' | ')
            print(f"{item['date_of_birth']}", end=' | ')
            print(f"Rank : {item['rank']}")

        print("\nSave to database ? [y/n] ", end='')

    @staticmethod
    def tournament_saved():
        print("\nTournament successfully saved to database !")

    @staticmethod
    def start_tournament_prompt():
        print("\nStart tournament now ? [y/n] ", end='')

    @staticmethod
    def select_players(players, player_number):
        """Display all players to select

        @param players: list of players
        @param player_number: number of current player for new tournament (if editing player == "")
        """
        print(f"\nSelect player {player_number} :\n")
        for i in range(len(players)):
            print(f"[{players[i]['id']}]", end=' ')
            print(f"{players[i]['last_name']}, {players[i]['first_name']}", end=" | ")
            print(f"{players[i]['gender']} | {players[i]['date_of_birth']}", end=" | ")
            print(f"Rank : {players[i]['rank']}")

        print("\n[back] Back to main menu")

    @staticmethod
    def select_tournament(tournaments):
        """Display all tournaments to select

        @param tournaments: tournaments list
        """
        print("\n" * 3 + "--- SELECT TOURNAMENT ---\n")

        for i in range(len(tournaments)):
            print(f"[{tournaments[i]['id']}]", end=' ')
            print(tournaments[i]['name'], end=' | ')
            print(tournaments[i]['location'], end=" | ")
            print(tournaments[i]['description'], end=' | ')
            print(f"Started on : {tournaments[i]['start_date']}", end=' | ')
            print(f"Ended on : {tournaments[i]['end_date']}", end=' | ')
            print(f"Round {tournaments[i]['current_round']-1}/{tournaments[i]['rounds_total']}")

        print("\n[back] Back to main menu")

    @staticmethod
    def create_new_player_header():
        print("\n" * 3 + "- NEW PLAYER -\n")

    @staticmethod
    def review_player(info):
        """Display all input info to review before saving to database

        @param info: player info list
        """
        print("\n\nNew player created :\n")
        print(f"{info[0]}, {info[1]}", end=' | ')
        print(f"Date of birth : {info[2]}", end=' | ')
        print(f"Gender : {info[3]}", end=' | ')
        print(f"Rank : {info[4]}")
        print("\nSave to database ? [y/n] ", end='')

    @staticmethod
    def update_player_info(p, options):
        """Player info editing prompts

        @param p: currently edited player
        @param options: editable options
        """
        print("\n\n--- UPDATE PLAYER INFO ---\n")
        print(f"Updating {p.last_name}, {p.first_name}\n")
        for i in range(len(options)):
            print(f"[{i+1}] Update {options[i]}")

        print("\n[back] Back to main menu")

    @staticmethod
    def player_saved():
        print("\nPlayer successfully saved to database !")

    @staticmethod
    def reports_menu():
        print("\n" * 3 + "--- REPORTS ---\n")
        print("[1] All players")
        print("[2] Players in a tournament")
        print("[3] All tournaments")
        print("[4] Rounds in a tournament")
        print("[5] Matches in a tournament")
        print("\n[back] Back to main menu")

    @staticmethod
    def reports_player_sorting():
        print("\n[1] Sort by name")
        print("[2] Sort by rank")
        print("\n[back] Back to main menu")

    @staticmethod
    def input_prompt_text(option):
        print(f"\nEnter {option} (type [back] for main menu) : ", end='')

    @staticmethod
    def input_prompt():
        print("\nType [option] and press Enter : ", end='')

    @staticmethod
    def are_you_sure_exit():
        print("\nAre you sure you want to exit the program ? [y/n] ", end='')

    @staticmethod
    def input_error():
        print("\nInput error, please enter a valid option.")

    @staticmethod
    def player_already_selected():
        print("\nPlayer already selected. Please select other player.")

    @staticmethod
    def other_report():
        print("\nWould you like to view another report ? [y/n] ", end='')

    @staticmethod
    def update_rank():
        print("\nUpdate ranks ? [y/n] ", end='')

    @staticmethod
    def rank_update_header(player):
        print(f"\nUpdating {player.last_name}, {player.first_name}")
