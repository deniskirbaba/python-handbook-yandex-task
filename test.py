print('Загадайте число от 1 до 1000000.')

start = 1
end = 1000000

while (end - start) > 1:
    middle = int((end + start) / 2)
    print('Ваше число больше чем', middle)
    answer = input()

    if answer == 'да':
        start = middle
    else:
        end = middle

print('Загаданное число:', end)

