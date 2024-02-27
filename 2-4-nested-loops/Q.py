n = int(input())

palindrome_n = 0

for i in range(n):
    s = input()
    L = len(s)
    if s[:L // 2] == s[(L + 1) // 2:][::-1]:
        palindrome_n += 1

print(palindrome_n)