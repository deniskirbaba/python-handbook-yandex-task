trials = 10
minmax = [1, 1000]

for i in range(trials):
    if minmax[0] == minmax[1]:
        guess = minmax[0]
    else:
        guess = minmax[0] + int((minmax[1] - minmax[0]) / 2)
    print(guess)
    
    match fb := input():
        case 'Больше':
            minmax[0] = guess + 1
        case 'Меньше':
            minmax[1] = guess - 1
        case 'Угадал!':
            break