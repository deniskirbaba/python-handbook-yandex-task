n = int(input())

names = dict()

for i in range(n):
    name = input()
    names[name] = names.get(name, 0) + 1

namesakes_flag = False

for name in sorted(list(names.keys())):
    if names[name] > 1:
        namesakes_flag = True
        print(f'{name} - {names[name]}')

if not namesakes_flag:
    print('Однофамильцев нет')
