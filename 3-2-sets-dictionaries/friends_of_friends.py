friends_1_lvl = dict()

while names := input().split():
    friends_1_lvl.setdefault(names[0], set()).add(names[1])
    friends_1_lvl.setdefault(names[1], set()).add(names[0])

friends_2_lvl = dict()
for name, friends in friends_1_lvl.items():
    friends_2_lvl[name] = set()
    for i in friends:
        friends_2_lvl[name] = friends_2_lvl[name] | friends_1_lvl[i]
    friends_2_lvl[name].discard(name)
    friends_2_lvl[name] = friends_2_lvl[name] - friends

for name in sorted(list(friends_2_lvl.keys())):
    print(f'{name}: {", ".join(sorted(list(friends_2_lvl[name])))}')
