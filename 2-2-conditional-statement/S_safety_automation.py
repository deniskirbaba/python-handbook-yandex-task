coordinates = [float(input()) for i in range(2)]

if (coordinates[0]**2 + coordinates[1]**2) <= 10**2:
    if ((5 >= coordinates[1] >= (0.25 * (coordinates[0] + 1)**2 - 9)) and 
            (coordinates[1] <= 5 / 3 * coordinates[0] + 35 / 3) and
            (((coordinates[0]**2 + coordinates[1]**2) <= 5**2) or (coordinates[0] < 0) or (coordinates[1] < 0))):
        print('Опасность! Покиньте зону как можно скорее!')
    else:
        print('Зона безопасна. Продолжайте работу.')
else:
    print('Вы вышли в море и рискуете быть съеденным акулой!')