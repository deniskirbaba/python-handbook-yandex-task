# decorator takes function as an argument
def count(f):
    total = 0

    # declare the function, that extends functionality of 'f'
    def decorated(*args, **kwargs):
        # 'total' declare as nonlocal in order to access from inner function
        nonlocal total
        total += 1
        # return result of initial function and additionally 'total'
        return f(*args, **kwargs), total
    # return new function as an object
    return decorated


@count
def hello(name):
    return f'Hello, {name}!'


print(hello("user_1"))
print(hello("user_2"))
