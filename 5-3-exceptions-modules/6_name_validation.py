import re


class CyrillicError(Exception):
    pass


class CapitalError(Exception):
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
    

# name_validation('24')
#print(name_validation('ПрполоджАшгнпоарстмьиболрдгнеаромтиотлшривет'))

# for i in range(ord('а'), ord('я') + 1):
#     print(chr(i))
# print(ord('я') - ord('а') + 1)

print(name_validation('ВВывааыв'))
