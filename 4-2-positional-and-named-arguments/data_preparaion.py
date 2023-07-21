def to_string(*args, sep=' ', end='\n'):
    return sep.join([str(i) for i in args]) + end


data = [7, 3, 1, "hello", (1, 2, 3)]
result = to_string(*data, sep=", ", end="!")
print(result)
