objects = dict()
while (s := input()) != '':
    for obj in s.split():
        objects[obj] = objects.get(obj, 0) + 1
for keys, values in objects.items():
    print(f'{keys} {values}')
