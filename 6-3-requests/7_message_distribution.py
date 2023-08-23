from requests import get
from sys import stdin


url = 'http://' + input() + '/users/' + input()
msg = stdin.read()
r = get(url)
if r.status_code == 404:
    print('Пользователь не найден')
else:
    for key, value in r.json().items():
        if key == 'id': value = str(value)
        msg = msg.replace(''.join(['{', key, '}']), value)
    print(msg)
