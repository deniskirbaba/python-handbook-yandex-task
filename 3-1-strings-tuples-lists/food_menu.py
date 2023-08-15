porridge = ('Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая')

n = int(input())

for i in range(n):
    print(porridge[i % len(porridge)])
