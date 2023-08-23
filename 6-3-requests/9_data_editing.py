from requests import put
from sys import stdin
from json import dumps


url = 'http://' + input() + '/users/' + input()
new_data = dict()
for line in stdin:
    key, value = line.rstrip().split('=')
    new_data[key] = value
put(url, data=dumps(new_data))
