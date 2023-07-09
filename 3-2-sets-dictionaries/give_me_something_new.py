n_available = int(input())
meals_available = set()
for i in range(n_available):
    meals_available.add(input())

n_prev_days = int(input())
meals_cooked = set()
for i in range(n_prev_days):
    n_meals = int(input())
    for j in range(n_meals):
        meals_cooked.add(input())

meals_to_cook = meals_available - meals_cooked

if len(meals_to_cook) > 0:
    for i in sorted(list(meals_to_cook)):
        print(i)
else:
    print('Готовить нечего')
