import re


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(name):
    if not isinstance(name, str):
        raise TypeError
    if not re.fullmatch('[a-zA-Z0-9_]+', name):
        raise BadCharacterError
    if name[0].isdigit():
        raise StartsWithDigitError
    return name


print(username_validation('f3sdaflk2409-dasf'))
