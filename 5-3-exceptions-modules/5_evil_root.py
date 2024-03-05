class EquationError(Exception):
    pass


class InfiniteSolutionsError(EquationError):
    pass


class NoSolutionsError(EquationError):
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
            return (-c / b, -c / b)
    else:
        d = b**2 - 4 * a * c
        if d < 0:
            raise NoSolutionsError
        elif d == 0:
            return (-b / (2 * a), -b / (2 * a))
        else:
            q1 = (-b - d**0.5) / (2 * a)
            q2 = (-b + d**0.5) / (2 * a)
            q = [q1, q2]
            q.sort()
            return (q[0], q[1])


# TypeError tests
# find_roots(1, 'adfs', 1)
# rational([4, '3.43'])

# InfiniteSolutionsError tests
# find_roots(0, 0, 0)

# NoSolutionsError tests
print(find_roots(0, 0, 1))
find_roots(1, 0, 2)

# print(find_roots(1, 2, 1))
# print(find_roots(0, 10, 0))

