import re


class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def is_cyrillic(s):
    return bool(re.fullmatch('[а-яёА-ЯЁ]+', s))


def is_title(s):
    return s == s.title()


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError
    if not is_cyrillic(name):
        raise CyrillicError
    if not is_title(name):
        raise CapitalError
    return name


def username_validation(name):
    if not isinstance(name, str):
        raise TypeError
    if not re.fullmatch('[a-zA-Z0-9_]+', name):
        raise BadCharacterError
    if name[0].isdigit():
        raise StartsWithDigitError
    return name


def user_validation(*args, last_name=None, first_name=None, username=None, **kwargs):
    if args != () or kwargs != {} or any(map(lambda x: x is None, (last_name, first_name, username))):
        raise KeyError
    name_validation(last_name)
    name_validation(first_name)
    username_validation(username)
    return {'last_name': last_name, 'first_name': first_name, 'username': username}


# print(user_validation(last_name='Кирбаба', first_name='Денис', username='kelces'))
print(user_validation(last_name="Иванов", first_name="Иван", username="ivanych45", password="123456"))
