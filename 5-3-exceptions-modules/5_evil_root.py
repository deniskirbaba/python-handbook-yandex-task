import math


class InfiniteSolutionsError(Exception):
    pass


class NoSolutionsError(Exception):
    pass


def rational(a):
    if not all(map(lambda x: isinstance(x, (float, int)), a)):
        raise TypeError


def find_roots(a, b, c):
    rational((a, b, c))
    if a == 0:
        if b == 0:
            if c == 0:
                raise InfiniteSolutionsError
            else:
                raise NoSolutionsError
        else:
            return (round(-c / b, 2), round(-c / b, 2))
    else:
        d = b**2 - 4 * a * c
        if d < 0:
            raise NoSolutionsError
        elif d == 0:
            return (round(-b / (2 * a), 2), round(-b / (2 * a), 2))
        else:
            q1 = (-b - math.sqrt(d)) / (2 * a)
            q2 = (-b + math.sqrt(d)) / (2 * a)
            q = [q1, q2]
            q.sort()
            return (round(q[0], 2), round(q[1], 2))


# TypeError tests
# find_roots(1, 'adfs', 1)
# rational([4, '3.43'])

# InfiniteSolutionsError tests
# find_roots(0, 0, 0)

# NoSolutionsError tests
# find_roots(0, 0, 1)
#find_roots(1, 0, 2)

# print(find_roots(1, 2, 1))
print(find_roots(0, 10, 0))

