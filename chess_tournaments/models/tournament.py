from tinydb import TinyDB


class Tournament:

    def __init__(
            self,
            t_id: int,
            name: str,
            location: str,
            start_date: str,
            end_date: str,
            description: str,
            time_control: str,
            current_round: int,
            players: list,
            rounds: list,
            rounds_total=4
    ):
        self.t_id = t_id
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.time_control = time_control
        self.current_round = current_round
        self.rounds_total = rounds_total
        self.players = players
        self.rounds = rounds

        self.tour_db = TinyDB('database/tournaments.json')

    def serialize_tournament(self):
        """Return serialized tournament info"""
        return {
            "id": self.t_id,
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "time_control": self.time_control,
            "current_round": self.current_round,
            "rounds_total": self.rounds_total,
            "players": self.players,
            "rounds": self.rounds,
        }

    def sort_players_by_rank(self):
        """Sort players by rank (ascending)"""
        self.players = sorted(self.players, key=lambda x: x.get('rank'))

    def sort_players_by_score(self):
        """Sort players by score (descending)"""
        self.players = sorted(self.players, key=lambda x: x.get('score'), reverse=True)

    def split_players(self):
        """Split player in 2 halves (top and bottom players)"""
        half = len(self.players) // 2
        return self.players[:half], self.players[half:]

    def merge_players(self, top_players, bottom_players):
        """Merge top and bottom players in order of matches

        @param top_players: top half of players (list)
        @param bottom_players: bottom half of players (list)
        """
        merged_players = []
        for i in range(len(self.players) // 2):
            merged_players.append(top_players[i])
            merged_players.append(bottom_players[i])

        self.players = merged_players

    def save_tournament_db(self):
        """Save new tournament to database
        Set tournament ID as document ID
        """
        db = self.tour_db
        self.t_id = db.insert(self.serialize_tournament())
        db.update({'id': self.t_id}, doc_ids=[self.t_id])

    def update_tournament_db(self):
        """Update tournament info (after each round) in database"""
        db = self.tour_db
        db.update({'rounds': self.rounds}, doc_ids=[self.t_id])
        db.update({'players': self.players}, doc_ids=[self.t_id])
        db.update({'current_round': self.current_round}, doc_ids=[self.t_id])

    def update_timer(self, timer, info):
        """Update start or end timer of tournament

        @param timer: date and time info (str)
        @param info: start or end time (str)
        """
        db = self.tour_db
        db.update({info: timer}, doc_ids=[self.t_id])

    @staticmethod
    def load_tournament_db():
        """Load tournament database

        @return: list of tournaments
        """
        db = TinyDB('database/tournaments.json')
        db.all()
        tournaments_list = []
        for item in db:
            tournaments_list.append(item)

        return tournaments_list
