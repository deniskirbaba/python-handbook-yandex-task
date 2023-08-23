from requests import get


url = 'http://' + input()
data = get(url).json()
res = data.get(input(), 'No data')
print(res)
