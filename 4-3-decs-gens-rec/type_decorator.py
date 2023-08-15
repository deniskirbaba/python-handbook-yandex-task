def same_type(f):
    def decorated(*args, **kwargs):
        if len(args) not in (0, 1):
            t = type(args[0])
            for i in range(1, len(args)):
                if not isinstance(args[i], t):
                    print('Обнаружены различные типы данных')
                    return
        return f(*args, **kwargs)
    return decorated


@same_type
def combine_text(*words):
    return ' '.join(words)


print(combine_text('Hello,', 'world!') or 'Fail')
print(combine_text(2, '+', 2, '=', 4) or 'Fail')
print(combine_text('Список из 30', 0, 'можно получить так', [0] * 30) or 'Fail')
