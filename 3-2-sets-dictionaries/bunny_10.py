near_bunny = set()

while terrain := input().split():
    for i, obj in enumerate(terrain):
        if obj == 'зайка':
            if i > 0:
                near_bunny.add(terrain[i - 1])
            if i < len(terrain) - 1:
                near_bunny.add(terrain[i + 1])

for obj in near_bunny:
    print(obj)
