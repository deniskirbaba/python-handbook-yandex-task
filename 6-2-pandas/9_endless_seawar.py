import numpy as np
import pandas as pd


ul, lr = [[int(i) for i in input().split()] for i in range(2)]

path = '6-2-pandas\data\data171_4fcbd1f963.csv'
data = pd.read_csv(path)

mask = (ul[0] <= data['x']) & (data['x'] <= lr[0]) & (lr[1] <= data['y']) & (data['y'] <= ul[1])
print(data[mask])
