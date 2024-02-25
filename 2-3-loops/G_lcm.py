from math import gcd

n1 = int(input())
n2 = int(input())

print(int(abs(n1 * n2) / gcd(n1, n2)))