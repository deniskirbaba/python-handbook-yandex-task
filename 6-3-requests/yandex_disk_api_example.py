from requests_oauthlib import OAuth2Session
from requests import get, post, put, delete


client_id = '55b1ae63462849eea7fe88a760be1008'
client_secret = '05f6c41bdfbf46f08eba30897fc8d653'
auth_url = 'https://oauth.yandex.ru/authorize'
token_url = 'https://oauth.yandex.ru/token'
oauth = OAuth2Session(client_id=client_id)
authorization_url, state = oauth.authorization_url(auth_url, force_confirm="true")
print("Перейдите по ссылке, авторизуйтесь и скопируйте код:", authorization_url)
code = input("Вставьте одноразовый код: ")
token = oauth.fetch_token(token_url=token_url,
                          code=code,
                          client_secret=client_secret)
access_token = token["access_token"]
print(access_token)

headers = {"Authorization": f"OAuth {access_token}"}
r = get("https://cloud-api.yandex.net/v1/disk", headers=headers)
print(r.json)
