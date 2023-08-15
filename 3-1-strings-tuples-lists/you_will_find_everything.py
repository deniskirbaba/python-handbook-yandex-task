n = int(input())

lists = list()
for i in range(n):
    lists.append(input())
query = input().lower().strip()
out = []
for i, s in enumerate(lists):
    if query in s.lower().strip():
        out.append(i)
for i in out:
    print(lists[i])
