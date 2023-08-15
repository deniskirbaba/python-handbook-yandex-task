def enter_results(*args):
    global data
    if 'data' not in globals():
        data = [[], []]
    data[0].extend(args[::2])
    data[1].extend(args[1::2])


def get_sum():
    return tuple((round(sum(i), 2) for i in data))


def get_average():
    return tuple((round(s / len(data[0]), 2) for s in get_sum()))


enter_results(3.5, 2.14, 45.2, 37.99)
print(get_sum(), get_average())
enter_results(5.2, 7.3)
print(get_sum(), get_average())
enter_results(1.23, 4.56, 3.14, 2.71, 0, 0)
print(get_sum(), get_average())
