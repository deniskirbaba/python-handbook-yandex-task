s = input().split()

flag = True
while flag:
    if len(s) == 1:
        print(s[0])
        break
    for i, ch in enumerate(s):
        if ch in '*-+':
            match ch:
                case '+':
                    res = int(s[i - 1]) + int(s[i - 2])
                case '*':
                    res = int(s[i - 1]) * int(s[i - 2])
                case '-':
                    res = int(s[i - 2]) - int(s[i - 1])
            del s[i]
            del s[i - 1]
            del s[i - 2]
            s.insert(i - 2, str(res))
            break
