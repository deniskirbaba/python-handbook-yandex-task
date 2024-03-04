# def split_numbers(s):
#     numbers = []
#     while (i := s.find(' ')) != -1:
#         numbers.append(int(s[:i]))
#         s = s[i + 1:]
#     numbers.append(int(s))
#     return tuple(numbers)

def split_numbers(s):
    return tuple([int(i) for i in s.split()])

result = split_numbers("1 2 3 4 5")
print(result)