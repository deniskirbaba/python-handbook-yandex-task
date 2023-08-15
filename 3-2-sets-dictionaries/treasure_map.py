n = int(input())

routes = dict()

for i in range(n):
    x, y = [int(i) // 10 for i in input().split()]
    routes[(x, y)] = routes.get((x, y), 0) + 1

print(max(routes.values()))
