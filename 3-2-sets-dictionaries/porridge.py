n_sem = int(input())
n_oat = int(input())

ch_sem = set()
ch_oat = set()

for i in range(n_sem):
    ch_sem.add(input())
for i in range(n_oat):
    ch_oat.add(input())

ch_both = ch_sem & ch_oat

n_both = len(ch_both)

if n_both == 0:
    print('Таких нет')
else:
    print(n_both)
