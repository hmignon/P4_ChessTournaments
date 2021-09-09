from tinydb import TinyDB


class Player:

    def __init__(
            self,
            p_id: int,
            last_name: str,
            first_name: str,
            birthday: str,
            gender: str,
            rank: int,
    ):
        self.p_id = p_id
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.gender = gender
        self.rank = rank
        self.score = 0.0
        self.opponents = []

        self.player_db = TinyDB('database/players.json')

    def serialize_player(self):
        """Return serialized player info"""
        return {
            "id": self.p_id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "date_of_birth": self.birthday,
            "gender": self.gender,
            "rank": self.rank,
            "score": self.score,
            "opponents": self.opponents
        }

    def save_player_db(self):
        """Save new player to database
        Set player ID as document ID
        """
        players_db = self.player_db
        self.p_id = players_db.insert(self.serialize_player())
        players_db.update({'id': self.p_id}, doc_ids=[self.p_id])

    def update_player_db(self, info, option):
        """Update player info (from user input) in database

        @param info: user input (str, or int inf "rank")
        @param option: update info category
        """
        db = self.player_db
        if option == "rank":
            db.update({option: int(info)}, doc_ids=[self.p_id])
        else:
            db.update({option: info}, doc_ids=[self.p_id])

    @staticmethod
    def load_player_db():
        """Load player database

        @return: list of players
        """
        players_db = TinyDB('database/players.json')
        players_db.all()
        players = []
        for item in players_db:
            players.append(item)

        return players
