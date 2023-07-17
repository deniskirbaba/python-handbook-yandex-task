from sys import stdin


def is_palindrome(word):
    word_len = len(word)
    # if (word_len % 2) == 0:
    #     return word[:word_len // 2] == word[word_len // 2:][::-1]
    # else:
    #     return word[:word_len // 2] == word[word_len // 2 + 1:][::-1]
    return word[:word_len // 2] == word[(word_len + 1) // 2:][::-1]


palindromes = set()
[palindromes.add(word) for word in stdin.read().split() if is_palindrome(word.lower())]
[print(palindrome) for palindrome in sorted(list(palindromes))]
