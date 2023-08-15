n_sem = int(input())
n_oat = int(input())

ch = set()
ch_one = set()

for i in range(n_oat + n_sem):
    name = input()
    if name not in ch:
        ch.add(name)
        ch_one.add(name)
    elif name in ch:
        ch_one.remove(name)

n_one = len(ch_one)

if n_one == 0:
    print('Таких нет')
else:
    for i in sorted(list(ch_one)):
        print(i)
