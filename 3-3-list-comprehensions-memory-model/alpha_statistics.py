text = input()

#letters_stat = {letter: freq for letter, freq in [(letter, text.count(letter)) for letter in text if letter.isalpha()]}
letters_stat = {letter: text.lower().count(letter) for letter in text.lower() if letter.isalpha()}

print(letters_stat)
