s = input()

L = len(s)

if s[:L // 2] == s[(L + 1) // 2:][::-1]:
    print('YES')
else:
    print('NO')
