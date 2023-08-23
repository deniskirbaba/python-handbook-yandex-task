from requests import get, ConnectionError


# response = get("https://static-maps.yandex.ru/1.x/?"
#              "ll=35,35&"
#              "spn=5,5&"
#              "l=map")
# print(response)
# with open('6-3-requests\data\map.png', mode='+wb') as file:
#     file.write(response.content)


# params = {'ll': '35,35',
#           'spn': '5,5',
#           'l': 'map'}
# response = get('https://static-maps.yandex.ru/1.x/', params=params)
# print(response)


# try:
#     params = {'ll': '35,35',
#             'spn': '5,5',
#             'l': 'map'}
#     response = get('https://static-maps.yandex.ru/1.x/', params=params)
# except ConnectionError as conerr:
#     print('Check connection.')
# else:
#     with open('6-3-requests\data\map.png', mode='+wb') as file:
#         file.write(response.content)
