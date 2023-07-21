string_1 = 'мама мыла раму'
string_2 = 'Яндекс использует Python во многих проектах'

print(sorted(string_1.split(), key=lambda w: (len(w), w)))
