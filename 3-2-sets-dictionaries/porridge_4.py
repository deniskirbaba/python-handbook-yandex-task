n = int(input())

porridge_data = dict()

for i in range(n):
    name_por = input().split()
    for j in range(len(name_por) - 1):
        porridge_data[name_por[j + 1]] = porridge_data.get(name_por[j + 1], []) + [name_por[0]]

query = input()

if porridge_data.get(query, 0) == 0:
    print('Таких нет')
else:
    for i in sorted(list(porridge_data[query])):
        print(i)
