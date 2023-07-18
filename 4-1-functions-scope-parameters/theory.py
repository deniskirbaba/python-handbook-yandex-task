# def only_even(numbers):
#     for x in numbers:
#         if x % 2 != 0:
#             return False
#     return True

# print(only_even([2, 4, 6, 8]))
# print(only_even([2, 4, 6, 9]))

# print(print('qqq'))

# def only_even(numbers):
#     for i, x in enumerate(numbers):
#         if x % 2 != 0:
#             return False, i
#     return True

# print(only_even([2, 4, 6, 8]))
# print(only_even([2, 4, 6, 9]))

def inc():
    global x
    x += 1
    print(f'Number of function calls: {x}')
x = 0
inc()
inc()
inc()
