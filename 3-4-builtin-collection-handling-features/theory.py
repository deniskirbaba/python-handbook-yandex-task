import itertools

# print(list(itertools.product('ABC', repeat=3)))

# for value in itertools.count(0, 0.1):
#     if value <= 1:
#         print(round(value, 1))
#     else:
#         break

# max_len = 10
# s = ""
# for value in itertools.cycle('ABC'):
#     if len(s) < 10:
#         s += value
#     else:
#         break
# print(s)

# print(list(itertools.repeat('ABC', 5)))

# for i in itertools.accumulate(range(5)):
#     print(i)

# for i in itertools.chain('abc', 'def', 'ghq'):
#     print(i)

# for i in itertools.chain.from_iterable(['abc', 'def', 'gh']):
#     print(i)

# for i in itertools.product(range(5), 'abcde', repeat=2):
#     print(i)
#
# for i in itertools.permutations('abcde', 2):
#     print(i)

# for i in itertools.combinations('abcde', 2):
#     print(i)

# for i in itertools.combinations_with_replacement('abcde', 2):
#     print(i)

# [print(idx, value) for idx, value in enumerate('abcdefg', 1)]

print(list(zip('abcdef', [1, 2, 3, 4])))
