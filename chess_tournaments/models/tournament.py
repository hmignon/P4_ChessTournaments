from tinydb import TinyDB


class Tournament:

    def __init__(
            self,
            name: str,
            location: str,
            start_date: str,
            end_date: str,
            description: str,
            time_control: str,
            current_round: int,
            rounds_total=4
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.time_control = time_control
        self.current_round = current_round
        self.rounds_total = rounds_total
        self.players = []
        self.matches = []

    def serialize_tournament(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "time_control": self.time_control,
            "current_round": self.current_round,
            "total_rounds": self.rounds_total,
            "players": self.players,
            "matches": self.matches
        }

    @staticmethod
    def load_tournament_db():
        db = TinyDB("database/tournaments.json")
        db.all()
        id_list = []
        tournaments_list = []
        for item in db:
            id_list.append(item.doc_id)
            tournaments_list.append(item)
        return tournaments_list, id_list

    def save_tournament_db(self):
        pass

    def update_tournament_db(self):
        pass
