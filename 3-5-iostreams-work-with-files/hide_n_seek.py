import os

path = '3-5-iostreams-work-with-files/data'
filename = 'secret.txt'

with open(os.path.join(path, filename), 'r', encoding='UTF-8') as fin:
    encoded_text = fin.read()
decoded_text = ''
for char in encoded_text:
    code = ord(char)
    if code >= 128:
        char = chr(code % 256)
    decoded_text += char
print(decoded_text)
