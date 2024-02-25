n = int(input())

first = None
for i in range(n):
    name = input()
    if first is None or name < first:
        first = name
print(first)