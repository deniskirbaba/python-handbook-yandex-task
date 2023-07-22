def result_accumulator(f):
    storage = []
    def decorated(*args, method='accumulate'):
        nonlocal storage
        storage.append(f(*args))
        if method == 'drop':
            res = storage.copy()
            storage.clear()
            return res
    return decorated


@result_accumulator
def get_letters(text: str) -> str:
    return ''.join(sorted(set(filter(str.isalpha, text.lower()))))


print(get_letters('Hello, world!'))
print(get_letters('Декораторы это круто =)'))
print(get_letters('Ехали медведи на велосипеде', method='drop'))

            