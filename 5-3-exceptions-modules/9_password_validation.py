import re
import hashlib
from string import ascii_letters, digits


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(pswd, 
                        min_length=8, 
                        possible_chars=ascii_letters + digits, 
                        at_least_one=str.isdigit):
    if not isinstance(pswd, str):
        raise TypeError
    if len(pswd) < min_length:
        raise MinLengthError
    if not all(map(lambda x: x in possible_chars, pswd)):
        raise PossibleCharError
    if not any(map(at_least_one, pswd)):
        raise NeedCharError
    return hashlib.sha256(bytes(pswd, 'utf-8')).hexdigest()
    

print(password_validation('dsaflkjsk0'))
print(password_validation("Hello12345"))
print(password_validation(
    "$uNri$e_777",
    min_length=6,
    at_least_one=lambda char: char in "!@#$%^&*()_"
))
