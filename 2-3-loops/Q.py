n = input()

new_n = ''
for i in n:
    if int(i) % 2 != 0:
        new_n += i

print(new_n)