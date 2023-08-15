def can_eat(horse_pos, enemy_pos):
    diff = [abs(i[0] - i[1]) for i in zip(horse_pos, enemy_pos)]
    return diff[0] == 1 and diff[1] == 2 or diff[0] == 2 and diff[1] == 1


print(can_eat((2, 2), (3, 4)))
