from tinydb import TinyDB


class DatabaseController:

    def __init__(self):
        self.tour_db = TinyDB('database/tournaments.json')
        self.player_db = TinyDB('database/players.json')

    """Tournament database"""
    def load_tournament_db(self):
        """Load tournament database

        @return: list of tournaments
        """
        db = self.tour_db
        db.all()
        tournaments_list = []
        for item in db:
            tournaments_list.append(item)

        return tournaments_list

    def save_tournament_db(self, tournament):
        """Save new tournament to database
        Set tournament ID as document ID

        @param tournament: tournament info list
        """
        db = self.tour_db
        t_id = db.insert(tournament.serialize_tournament())
        db.update({'id': t_id}, doc_ids=[t_id])

    def update_tournament_db(self, id_num, rounds, players, round_num):
        """Update tournament info (after each round) in database

        @param id_num: tournament ID == document ID (int)
        @param rounds: rounds data (list)
        @param players: players data (list)
        @param round_num: current round number (int)
        """
        db = self.tour_db
        db.update({'rounds': rounds}, doc_ids=[id_num])
        db.update({'players': players}, doc_ids=[id_num])
        db.update({'current_round': round_num}, doc_ids=[id_num])

    def update_timer(self, id_num, timer, info):
        """Update start or end timer of tournament

        @param id_num: tournament ID == document ID (int)
        @param timer: date and time info (str)
        @param info: start or end time (str)
        """
        db = self.tour_db
        db.update({info: timer}, doc_ids=[id_num])

    """Player database"""
    def load_player_db(self):
        """Load player database

        @return: list of players
        """
        players_db = self.player_db
        players_db.all()
        players = []
        for item in players_db:
            players.append(item)

        return players

    def save_player_db(self, player):
        """Save new player to database
        Set player ID as document ID

        @param player: player info list
        """
        players_db = self.player_db
        p_id = players_db.insert(player.serialize_player())
        players_db.update({'id': p_id}, doc_ids=[p_id])

    def update_player_db(self, player, info, option):
        """Update player info (from user input) in database

        @param player: player (dict) being updated
        @param info: user input (str, or int inf "rank")
        @param option: update info category
        """
        db = self.player_db
        if option == "rank":
            db.update({option: int(info)}, doc_ids=[int(player["id"])])
        else:
            db.update({option: info}, doc_ids=[int(player["id"])])
