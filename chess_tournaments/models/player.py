from tinydb import TinyDB


class Player:

    def __init__(
            self,
            last_name: str,
            first_name: str,
            birthday: str,
            gender: str,
            rank: int,
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.gender = gender
        self.rank = rank
        self.score = 0.0
        self.opponents = []

    def serialize_player(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "date_of_birth": self.birthday,
            "gender": self.gender,
            "rank": self.rank,
            "score": self.score,
            "opponents": self.opponents
        }

    def add_player(self, player_info):
        pass

    def update_name(self, new_last_name, new_first_name):
        self.last_name = new_last_name
        self.first_name = new_first_name
        return self.last_name, self.first_name

    def update_birthday(self, new_birthday):
        self.birthday = new_birthday
        return self.birthday

    def update_gender(self, new_gender):
        self.gender = new_gender
        return self.gender

    def update_rank(self, new_rank: int):
        self.rank = new_rank
        # TODO inverser avec le rang remplacé
        return self.rank

    @staticmethod
    def load_player_db():
        players_db = TinyDB('database/players.json')
        players_db.all()
        id_list = []
        players = []
        for item in players_db:
            if len(str(item.doc_id)) == 1:
                id_list.append("0" + str(item.doc_id))
            else:
                id_list.append(str(item.doc_id))
            players.append(item)

        return players, id_list

    def update_player_db(self):
        pass

    def save_player_db(self):
        players_db = TinyDB('database/players.json')
        players_db.insert(self.serialize_player())

    @staticmethod
    def sort_players_name(players):
        players = sorted(players, key=lambda x: x.get('last_name'))
        return players

    @staticmethod
    def sort_players_rank(players):
        players = sorted(players, key=lambda x: x.get('rank'))
        return players
