"""
----------------------------------------
    CHESS TOURNAMENT - SWISS SYSTEM
----------------------------------------
First version : chess tournament with set of 8 predefined players.

"""


def first_round():
    """FIRST ROUND :
    Matches between top players and bottom players in order of rank.

    """
    players = [
        {'name': 'Lucien Lamarre', 'ranking': 5, 'score': 0.0, 'opponents': []},
        {'name': 'Capucine Dupuy', 'ranking': 1, 'score': 0.0, 'opponents': []},
        {'name': 'Pierre Hubert', 'ranking': 3, 'score': 0.0, 'opponents': []},
        {'name': 'Rodrigue Gagnon', 'ranking': 8, 'score': 0.0, 'opponents': []},
        {'name': 'Gaëtan Fortier', 'ranking': 2, 'score': 0.0, 'opponents': []},
        {'name': 'Marjolaine Perrin', 'ranking': 7, 'score': 0.0, 'opponents': []},
        {'name': 'Georgette Lachance', 'ranking': 6, 'score': 0.0, 'opponents': []},
        {'name': 'Jacques Picard', 'ranking': 4, 'score': 0.0, 'opponents': []}
    ]
    rounds = len(players) // 2

    print("- ROUND 1 -")
    top_players, bottom_players = split_players(sort_players_by_rank(players))

    for i in range(rounds):
        print("\nMatch " + str(i+1) + " :")
        next_match = str(top_players[i]) + " vs. " + str(bottom_players[i])
        print(next_match)
        top_players[i]["opponents"].append(bottom_players[i]["name"])
        bottom_players[i]["opponents"].append(top_players[i]["name"])

    top_players, bottom_players = get_score_first_round(rounds, top_players, bottom_players)
    players = top_players + bottom_players

    round_index = 2
    while round_index <= rounds:
        print("- ROUND " + str(round_index) + " -")
        players = sort_players_by_score(players)
        players = next_rounds(rounds, players)
        round_index += 1
    display_results(players)


def sort_players_by_rank(players):
    """Sort players by value of 'ranking' key.

    :param players: list of players dicts
    :return: list of players dicts sorted by rank
    """
    players = sorted(players, key=lambda x: x.get('ranking'))
    return players


def split_players(players):
    """Split players into 2 top and bottom halves.

    :param players: list of players dicts
    :return: top players dicts list, bottom players dicts list
    """
    half = len(players) // 2
    return players[:half], players[half:]


def get_score_first_round(rounds, top_players, bottom_players):
    """User input scores for first round.
    Update player 'score' key value according to scoring scheme.

    :param rounds: int. amount of rounds (players / 2)
    :param top_players: top players dicts list
    :param bottom_players: bottom players dicts list
    :return: top players dicts list, bottom players dicts list (scores updated)
    """
    for i in range(rounds):
        print("\nMatch ", i + 1)
        print('[0] Draw')
        print('[1] Player 1 wins')
        print('[2] Player 2 wins')
        response = input('Who won ?')
        if response == "0":
            (top_players[i])["score"] += 0.5
            (bottom_players[i])["score"] += 0.5
        elif response == "1":
            (top_players[i])["score"] += 1.0
        elif response == "2":
            (bottom_players[i])["score"] += 1.0

    return top_players, bottom_players


def sort_players_by_score(players):
    """Sort by rank again.
    Sort players by value of 'score' key.

    :param players: list of players dicts
    :return: list of players dicts sorted by rank and score
    """
    players = sort_players_by_rank(players)
    players = sorted(players, key=lambda x: x.get('score'), reverse=True)
    return players


def next_rounds(rounds, players):
    """NEXT ROUNDS:
    Matches between players sorted by score.
    Matches are set according to P1 vs. P2, P3 vs. P4, etc...
    If match already played (added to player's opponents list),
    try P1 vs. P3, etc...
    If not available, play first match option, regardless of match history.

    :param rounds: int. amount of rounds (players / 2)
    :param players: list of players dicts
    :return: list of players dicts with updated score for next round
    """
    available_list = players
    players_added = []
    k = 0

    while k < rounds:
        print("\nMatch " + str(k+1) + " :")
        if available_list[1]["name"] not in available_list[0]["opponents"]:
            available_list, players_added = match_first_option(available_list, players_added)

        elif available_list[1]["name"] in available_list[0]["opponents"]:
            try:
                available_list, players_added = match_second_option(available_list, players_added)
            except IndexError:
                available_list, players_added = match_first_option(available_list, players_added)

        k += 1

    players_added = update_scores(players_added, (get_round_scores(rounds)))
    players = players_added
    return players


def match_first_option(available_list, players_added):
    """Main match option : P1 vs. P2...
    For each match :
    - Display match title
    - Add both players to list of unavailable players ("already in a match")
    - Add player's name to opponent's played list
    - Remove players from available players ("not currently set in a match").

    :param available_list: list of available players ("not currently in a match")
    :param players_added: list of unavailable players ("already in a match")
    :return: available_list, players_added
    """
    next_match = str(available_list[0]) + " vs. " + str(available_list[1])
    print(next_match)

    players_added.extend([available_list[0], available_list[1]])
    available_list[1]["opponents"].append(available_list[0]["name"])
    available_list[0]["opponents"].append(available_list[1]["name"])
    available_list.remove(available_list[1])
    available_list.remove(available_list[0])

    return available_list, players_added


def match_second_option(available_list, players_added):
    """Second match option : P1 vs. P3...
    For each match :
    - Display match title
    - Add both players to list of unavailable players ("already in a match")
    - Add player's name to opponent's played list
    - Remove players from available players ("not currently set in a match").

    :param available_list: list of available players ("not currently in a match")
    :param players_added: list of unavailable players ("already in a match")
    :return: available_list, players_added
    """
    next_match = str(available_list[0]) + " vs. " + str(available_list[2])
    print(next_match)

    players_added.extend([available_list[0], available_list[2]])
    available_list[2]["opponents"].append(available_list[0]["name"])
    available_list[0]["opponents"].append(available_list[2]["name"])
    available_list.remove(available_list[2])
    available_list.remove(available_list[0])

    return available_list, players_added


def get_round_scores(rounds):
    """User input scores for round.
    Add player scores to list of scores.

    :param rounds: int. amount of rounds (players / 2)
    :return: list of scores (type float)
    """
    scores_list = []
    for i in range(rounds):
        print("\nMatch ", i + 1)
        print('[0] Draw')
        print('[1] Player 1 wins')
        print('[2] Player 2 wins')
        response = input('\nWho won ? \n')
        if response == "0":
            scores_list.extend([0.5, 0.5])
        elif response == "1":
            scores_list.extend([1.0, 0.0])
        elif response == "2":
            scores_list.extend([0.0, 1.0])

    return scores_list


def update_scores(players_added, scores_list):
    """Update scores :
    add points in scores_list index to value of key 'score' in players index.

    :param players_added: list of unavailable players (complete)
    :param scores_list: list of scores (type float)
    :return: list of players dicts (updated scores)
    """
    for i in range(len(players_added)):
        players_added[i]["score"] += scores_list[i]
    return players_added


def display_results(players):
    """END OF TOURNAMENT :
    Sort players by score.
    Display player name + score (descending)
    :param players: list of players dicts
    """
    players = sort_players_by_score(players)
    print("\n\n- FINAL SCORES -\n")
    for i in range(len(players)):
        print(str(players[i]['name']), "=", end=' ')
        print(str(players[i]['score']) + " pts")


if __name__ == "__main__":
    first_round()
