n = int(input())

objects = set()
for i in range(n):
    objects = objects | set(input().split())

for i in objects:
    print(i)
