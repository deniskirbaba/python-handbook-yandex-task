from requests import delete


url = 'http://' + input() + '/users/' + input()
delete(url)