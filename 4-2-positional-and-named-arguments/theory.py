# def final_price(price, discount=1):
#     return price * (1 - discount / 100)
# print(final_price(100, 10))
# print(final_price(100))


# def add_value(x, list_arg=[]):
#     list_arg += [x]
#     return list_arg
# print(add_value(0))
# print(add_value(0, [1, 2, 3]))
# print(add_value(1))
# print(add_value(2))


# def add_value(x, list_arg=None):
#     if list_arg is None:
#         list_arg = []
#     list_arg += [x]
#     return list_arg
# print(add_value(0))
# print(add_value(0, [1, 2, 3]))
# print(add_value(1))
# print(add_value(2))


# def final_price(price, discount=1):
#     return price * (1 - discount / 100)
# print(final_price(100, discount=10))
# print(final_price(discount=10, price=100))


# def final_price(*prices, discount=1):
#     return [price * (1 - discount / 100) for price in prices]
# print(final_price(100, 200, 300, discount=10))


# def final_price(*prices, discount=1, **kwargs):
#     low = kwargs.get('price_low', min(prices))
#     high = kwargs.get('price_high', max(prices))
#     return [price * (1 - discount / 100) for price in prices if low <= price <= high]
# print(final_price(100, 200, 300, 400, 500, discount=5))
# print(final_price(100, 200, 300, 400, 500, discount=5, price_low=200))
# print(final_price(100, 200, 300, 400, 500, discount=5, price_high=200))
# print(final_price(100, 200, 300, 400, 500, discount=5, price_low=200, price_high=350))


# def only_pos(x):
#     return x > 0
# result = filter(only_pos, range(-5, 5))
# print(list(result))


# result = filter(str.isalpha, "salkfd2490209400-024a;sdlkfj")
# print(list(result))


# def square(x):
#     return x ** 2
# result = map(square, range(10))
# print(list(result))


# result = map(str.title, ['sdfkl', 'lsadfj'])
# print(list(result))


# numbers = map(int, input().split())
# print(list(numbers))


# lambda x: x > 0


# result = filter(lambda x: x > 0, range(-5, 5))
# print(list(result))


# result = map(lambda x: x**2, range(0, 10))
# print(list(result))


# lines = ['sadf', 'k', 'es', 'a', 'asd;lfrfa', 'as', 'bs', 'x']
# result = sorted(lines, key=lambda s: len(s))
# print(result)
# result = sorted(lines, key=lambda s: (len(s), s))
# print(result)
# result = sorted(lines, key=lambda s: (-len(s), s))
# print(result)


# lines = ['bbcd', 'k', 'es', 'a', 'abcd', 'as', 'bs', 'x']
# print(min(lines), max(lines))
# print(max(lines, key=lambda s: (-len(s), s)))


from functools import reduce
numbers = range(1, 6)
print(reduce(lambda x, y: x + y, numbers))
print(sum(numbers))
