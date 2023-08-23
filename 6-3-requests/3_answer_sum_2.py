from requests import get


url = 'http://' + input()
data = get(url).json()
res = 0
for i in data:
    if isinstance(i, int):
        res += i
print(res)
