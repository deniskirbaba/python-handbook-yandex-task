n = int(input())

symbols = ('а', 'б', 'в')
flag = True
for i in range(n):
    if not input().lower().startswith(symbols):
        flag = False
if flag:
    print("YES")
else:
    print("NO")
