n = int(input())
m = int(input())

petya = 7
vasya = 6

petya -= 3
vasya += 3
petya += 2

vasya += 5
vasya -= 2

petya += n
vasya += m

if petya > vasya:
    print('Петя')
else:
    print('Вася')
    