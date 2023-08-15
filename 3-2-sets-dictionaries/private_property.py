unique = set()
not_unique = set()

n = int(input())

for i in range(n):
    name, toys = [i for i in input().split(': ')]
    toys = set(toys.split(', '))
    for toy in toys:
        if toy not in (unique | not_unique):
            unique.add(toy)
        elif toy in unique:
            unique.discard(toy)
            not_unique.add(toy)

print('\n'.join(sorted(list(unique))))
