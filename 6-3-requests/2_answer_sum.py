from requests import get


url = 'http://' + input()
res = 0
while (r := int(get(url).content)) != 0:
    res += r
print(res)
