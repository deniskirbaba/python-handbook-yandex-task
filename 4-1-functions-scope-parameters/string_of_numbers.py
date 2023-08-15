def split_numbers(s):
    numbers = []
    while (i := s.find(' ')) != -1:
        numbers.append(int(s[:i]))
        s = s[i + 1:]
    numbers.append(int(s))
    return tuple(numbers)