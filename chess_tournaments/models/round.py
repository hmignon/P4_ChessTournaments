class Round:

    def __init__(
            self,
            round_name: str,
            start_datetime: str,
            end_datetime: str
    ):
        self.round_name = round_name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.matches = []

    def set_round(self):
        """Return round info as list"""
        return [
            self.round_name,
            self.start_datetime,
            self.end_datetime,
            self.matches
        ]

    def get_match_pairing(self, player_1, player_2):
        """Set match paring as tuple"""
        match = (
            f"{player_1['last_name']}, {player_1['first_name']}",
            player_1["rank"],
            player_1["score"],
            f"{player_2['last_name']}, {player_2['first_name']}",
            player_2["rank"],
            player_2["score"]
        )
        self.matches.append(match)
