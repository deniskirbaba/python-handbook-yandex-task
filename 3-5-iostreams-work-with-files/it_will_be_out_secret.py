import os

shift = int(input()) % 26  # now only forward shifting
input_fn = 'public.txt'
output_fn = 'private.txt'
path = '3-5-iostreams-work-with-files/data'

with open(os.path.join(path, input_fn), 'r', encoding='UTF-8') as fin:
    msg = fin.read()
encoded_msg = ''
if shift == 0:
    encoded_msg = msg
else:
    for ch in msg:
        if ch.isalpha():
            lower = ch.islower()
            code = ord(ch.upper())
            ch = chr((code - 65 + shift) % 26 + 65)
        if lower:
            ch = ch.lower()
        encoded_msg += ch
with open(os.path.join(path, output_fn), 'w', encoding='UTF-8') as fout:
    print(encoded_msg, file=fout)
