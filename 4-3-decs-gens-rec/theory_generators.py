# function-generator for Fibonacci sequence
def fib(n):
    n_1, n_2 = 1, 1
    for i in range(n):
        yield n_1
        n_1, n_2 = n_2, n_1 + n_2


print(", ".join(str(x) for x in fib(10)))
