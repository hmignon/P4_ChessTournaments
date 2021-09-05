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
        self.players = sorted(self.players, key=lambda x: x.get('rank'))
        return self.players

    def sort_players_by_score(self):
        self.players = sorted(self.players, key=lambda x: x.get('score'), reverse=True)
        return self.players

    def split_players(self):
        half = len(self.players) // 2
        return self.players[:half], self.players[half:]
