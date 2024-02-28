s = input().replace(' ','').lower()
if s[:len(s) // 2] == s[-1:(len(s) - 1) // 2:-1]:
    print('YES')
else:
    print('NO')