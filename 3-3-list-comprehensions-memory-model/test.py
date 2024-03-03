# numbers = [int(input()) for i in range(5)]
# avg = sum(numbers) // len(numbers)
# numbers = [element for element in numbers if element > avg]
# print(numbers)

# matrix = [[int(i) for i in input().split()] for i in range(5)]
# print(matrix)

# zeros = [[0] * 5] * 5
# zeros[0][1] = 1
# print(zeros)

# zeros = [[0] * 5 for i in range(5)]
# zeros[0][1] = 1
# print(zeros)

# text = 'Cristiano Ronaldo'
# syms = [ord(symbol) for symbol in text]
# print(syms)

# countries = {"Россия": ["русский"],
#              "Беларусь": ["белорусский", "русский"],
#              "Бельгия": ["немецкий", "французский", "нидерландский"],
#              "Вьетнам": ["вьетнамский"]}
# uni_lang_countries = [country for (country, languages) in countries.items() if len(languages) == 1]
# print(uni_lang_countries)

# numbers = (int(input()) for i in range(5))
# print(numbers)
#
# countries = {"Россия": ["русский"],
#              "Беларусь": ["белорусский", "русский"],
#              "Бельгия": ["немецкий", "французский", "нидерландский"],
#              "Вьетнам": ["вьетнамский"]}
# countries_iter = iter(countries)
# print(iter(countries))

from sys import getsizeof

# print(getsizeof(countries), getsizeof(countries_iter))

# num = (i for i in range(10**6))
# num_list = list(range(10**6))
# print(getsizeof(num), getsizeof(num_list))
# print(getsizeof(num_list) / 10**6)

from timeit import timeit

x = 5
print(id(x))
y = x
print(id(y))
x = 6
print(x, y)
print(id(x), id(y))
# print(y is x)

# l = [1, 2, 3]
# print(id(l))
# l.append(4)
# print(id(l))
# l += [5]
# print(id(l))
# l = l + [6]
# print(id(l))

# mat = [[i + j for i in range(1, 4)] for j in [0, 3, 6]]
# print(mat)
# mat_copy = mat[:]
# print(mat_copy)
