class Round:

    def __init__(self):
        pass

    @classmethod
    def sort_players_by_rank(cls, players):
        players = sorted(players, key=lambda x: x.get('rank'))
        return players

    @classmethod
    def split_players(cls, players):
        half = len(players) // 2
        return players[:half], players[half:]

    @classmethod
    def next_rounds(cls):
        pass

    @classmethod
    def get_score(cls, response, scores_list):
        if response == "0":
            scores_list.extend([0.5, 0.5])
        elif response == "1":
            scores_list.extend([1.0, 0.0])
        elif response == "2":
            scores_list.extend([0.0, 1.0])

        return scores_list

    @classmethod
    def update_scores(cls, players, scores_list):
        for i in range(len(players)):
            players[i]["score"] += scores_list[i]

        return players

    @staticmethod
    def sort_players_by_score(players):
        players = sorted(players, key=lambda x: x.get('score'), reverse=True)

        return players

    @staticmethod
    def update_opponents(player1, player2):
        player1["opponents"].append(player2["id"])
        player2["opponents"].append(player1["id"])

        return player1, player2

    @staticmethod
    def update_player_lists(player1, player2, available_list, players_added):
        players_added.extend([player1, player2])
        available_list.remove(player1)
        available_list.remove(player2)

        return available_list, players_added
