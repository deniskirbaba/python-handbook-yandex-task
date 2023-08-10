import numpy as np
import pandas as pd
from string import punctuation, digits


words = input().translate({ord(i): None for i in punctuation + digits}).lower().split()
words = sorted([*set(words)])
lengths = pd.Series([len(i) for i in words], index=words)
print(lengths)
