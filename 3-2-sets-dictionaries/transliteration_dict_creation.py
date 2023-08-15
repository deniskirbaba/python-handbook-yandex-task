transliteration = dict()
while (s := input()) != '':
    rus, dash, eng = s.split()
    transliteration[rus] = eng
print(transliteration)
