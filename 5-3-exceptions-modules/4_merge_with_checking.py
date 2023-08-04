from itertools import chain


def if_iterible(a):
    try:
        iter(a)
    except TypeError:
        raise StopIteration


def if_homogeneous(a):
    t = type(a[0])
    if not all(map(lambda x: type(x) == t, a)):
        raise TypeError
    

def if_sorted(a):
    prev = a[0]
    for i in a[1:]:
        if i < prev:
            raise ValueError
        prev = i


def merge(a, b):
    [if_iterible(i) for i in (a, b)]
    if_homogeneous(list(chain(a, b)))
    [if_sorted(i) for i in (a, b)]

    res = []
    a_idx = 0
    b_idx = 0
    for i in range(len(a) + len(b)):
        if a_idx == len(a):
            res.extend(b[b_idx:])
            break
        elif b_idx == len(b):
            res.extend(a[a_idx:])
            break
        if a[a_idx] <= b[b_idx]:
            res.append(a[a_idx])
            a_idx += 1
        else:
            res.append(b[b_idx])
            b_idx += 1
    return tuple(res)


# StopIteration exception tests
# print(merge(4, 4))
# print(merge(range(5), 4))
# print(merge(4, range(5)))
# print(merge('abcd', ['a', 'b']))
# print(merge(('aa', 'bb'), ('aaa', 'bbb')))

# TypeError exception tests
# print(merge([1, 'dsf'], range(5)))
# print(merge(range(5), ['a', 'b']))

# ValueError exception tests
print(merge(range(5, 0, -1), range(5)))
