from tinydb import TinyDB


class DatabaseController:

    def __init__(self):
        self.tour_db = TinyDB('database/tournaments.json')
        self.player_db = TinyDB('database/players.json')

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
