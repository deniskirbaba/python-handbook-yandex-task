user = {'id': 1,
        'name': 'Den',
        'surname': 'Kirbaba'}
msg = 'Hello, this msg for {name} {surname}!'
for key, value in user.items():
    msg = msg.replace(''.join(['{', key, '}']), value)
print(msg)
