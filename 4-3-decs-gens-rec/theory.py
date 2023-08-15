# def fact(n):
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res

# print(fact(5))


# def fact(n):
#     if n == 0:
#         return 1
#     return fact(n - 1) * n

# print(fact(0))


# from timeit import timeit

# def fib(n):
#     if n in (0, 1):
#         return 1
#     return fib(n - 1) + fib(n - 2)

# print(f"Average time of calculating: "
#       f"{round(timeit('fib(35)', number=10, globals=globals()) / 10, 3)} sec.")


# from timeit import timeit

# def fib(n):
#     f_1, f = 1, 1
#     for i in range(n - 1):
#         f_1, f = f, f_1 + f
#     return f
# print('Average time of calculation: '
#       f'{round(timeit("fib(35)", number=10, globals=globals()) / 10, 3)} sec.')


# def fib(n):
#     global count
#     count += 1
#     if n in (0, 1):
#         return 1
#     return fib(n - 1) + fib(n - 2)

# count = 0
# print(fib(35))
# print(count)


# from timeit import timeit

# def fib(n):
#     global count
#     count += 1
#     if n not in cash:
#         cash[n] = fib(n - 1) + fib(n - 2)
#     return cash[n]

# count = 0
# cash = {0: 1, 1: 1}
# # print(fib(35))
# # print(count)
# # print(f"{round(timeit('fib(35)', number=10, globals=globals()) / 10, 3)} sec.")

# from sys import setrecursionlimit
# setrecursionlimit(2000)
# print(fib(1500))
#print(fib(1000))


from timeit import timeit
from functools import lru_cache

@lru_cache(maxsize=2000)
def fib(n):
    if n in (0, 1):
        return 1
    return fib(n - 1) + fib(n - 2)

print('Average time of calculation: '
      f'{round(timeit("fib(35)", number=10, globals=globals()) / 10, 3)} sec.')
