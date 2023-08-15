import numpy as np
import pandas as pd
from string import digits, punctuation


def length_stats(text):
    words = text.lower().translate({ord(i): None for i in digits + punctuation}).split()
    words = sorted([*set(words)])
    even_stats = pd.Series({word: len(word) for word in words if len(word) % 2 == 0}, dtype=np.int64)
    odd_stats = pd.Series({word: len(word) for word in words if len(word) % 2 != 0}, dtype=np.int64)
    return odd_stats, even_stats


odd, even = length_stats('Мама мыла раму')
print(odd)
print(even)



