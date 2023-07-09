transliteration = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'ZH', 'З': 'Z', 'И': 'I',
                   'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
                   'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ы': 'Y', 'Э': 'E',
                   'Ю': 'IU', 'Я': 'IA'}

rus = input()
eng = ''
for char in rus:
    if char not in 'ЪЬъь':
        if char.upper() in transliteration:
            lower = char.islower()
            if lower:
                eng += transliteration[char.upper()].lower()
            else:
                eng += transliteration[char.upper()].title()
        else:
            eng += char

print(eng)
