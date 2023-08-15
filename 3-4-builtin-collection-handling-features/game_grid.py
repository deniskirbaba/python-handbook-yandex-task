from itertools import combinations

n = int(input())
participants = [input() for i in range(n)]

[print(f'{player_1} - {player_2}') for player_1, player_2 in combinations(participants, 2)]
