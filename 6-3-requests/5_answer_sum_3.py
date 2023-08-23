from sys import stdin
from requests import get


url = 'http://' + input()
res = 0
for line in stdin:
    res += sum(get(url + line.rstrip()).json())
print(res)
