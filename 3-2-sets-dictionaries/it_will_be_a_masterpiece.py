n_available_products = int(input())
available_products = set()
for i in range(n_available_products):
    available_products.add(input())

n_recipes = int(input())
recipes = dict()
for i in range(n_recipes):
    meal_name = input()
    recipes[meal_name] = set()
    n_ingredients = int(input())
    for j in range(n_ingredients):
        recipes[meal_name].add(input())

available_meals = list()
for meal, ingredients in recipes.items():
    if available_products >= ingredients:
        available_meals.append(meal)

if len(available_meals) > 0:
    for i in sorted(available_meals):
        print(i)
else:
    print('Готовить нечего')

