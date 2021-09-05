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
