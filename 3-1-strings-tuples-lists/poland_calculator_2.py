from math import factorial

s = input().split()

flag = True
while flag:
    if len(s) == 1:
        print(s[0])
        break
    for i, ch in enumerate(s):
        if ch in '*-+/':
            match ch:
                case '+':
                    res = int(s[i - 1]) + int(s[i - 2])
                case '*':
                    res = int(s[i - 1]) * int(s[i - 2])
                case '-':
                    res = int(s[i - 2]) - int(s[i - 1])
                case '/':
                    res = int(s[i - 2]) // int(s[i - 1])
            del s[i]
            del s[i - 1]
            del s[i - 2]
            s.insert(i - 2, str(res))
            break
        elif ch in '~!':
            match ch:
                case '~':
                    res = -int(s[i - 1])
                case '!':
                    res = factorial(int(s[i - 1]))
            del s[i]
            del s[i - 1]
            s.insert(i - 1, str(res))
            break
        elif ch == '#':
            del s[i]
            s.insert(i - 1, s[i - 1])
            break
        elif ch == '@':
            res = s[i - 3]
            del s[i]
            del s[i - 3]
            s.insert(i - 1, res)
            break
