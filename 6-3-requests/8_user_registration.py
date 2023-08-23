from requests import post
from json import dumps


url = 'http://' + input() + '/users'
new_user = {'username': input(),
            'last_name': input(),
            'first_name': input(),
            'email': input()}
post(url, data=dumps(new_user))
