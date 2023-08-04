def only_positive_even_sum(a, b):
    try:
        if not all((isinstance(i, int) for i in (a, b))):
            raise TypeError('TypeError')
        if not all((i > 0 and i % 2 == 0 for i in (a, b))):
            raise ValueError('ValueError')
    except TypeError as e:
        return f'Вызвано исключение {e}'
    except ValueError as e:
        return f'Вызвано исключение {e}'
    else:
        return a + b


print(only_positive_even_sum(2, 4))
