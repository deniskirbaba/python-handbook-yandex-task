from requests import get


url = 'http://' + input() + '/users'
data = get(url).json()
for user in sorted(data, key=lambda i: ' '.join([i['last_name'], i['first_name']])):
    print(' '.join([user['last_name'], user['first_name']]))
