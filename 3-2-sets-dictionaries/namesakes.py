n = int(input())
names = dict()
for i in range(n):
    name = input()
    names[name] = names.get(name, 0) + 1
n_namesakes = 0
for i in names.values():
    if i > 1:
        n_namesakes += i
print(n_namesakes)
