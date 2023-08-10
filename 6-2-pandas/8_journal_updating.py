import numpy as np
import pandas as pd


def update(data: pd.DataFrame):
    data['average'] = data.mean(axis=1, numeric_only=True)
    data.sort_values(['average', 'name'], ascending=[False, True], inplace=True)
    return data


columns = ['name', 'maths', 'physics', 'computer science']
data = {
    'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев', 'Бобров'],
    'maths': [5, 4, 5, 2, 4, 5],
    'physics': [4, 4, 4, 5, 5, 4],
    'computer science': [5, 2, 5, 4, 3, 5]
}
journal = pd.DataFrame(data, columns=columns)
filtered = update(journal)
print(journal)
print(filtered)
