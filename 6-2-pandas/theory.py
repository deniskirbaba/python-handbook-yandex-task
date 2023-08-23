import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


s = pd.Series(np.arange(10, 13), index=['a', 'b', 'c'])
# print(s)
# print(s[1:])
# print(s.index)


# s = pd.Series(data, index=index)
# s = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
# print(s)
# print()
# s = pd.Series(np.linspace(0, 1, 5))
# print(s)


# d = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# print(pd.Series(d))
# print()
# print(pd.Series(d, index=['a', 'b', 'c', 'g']))


# index = ["a", "b", "c"]
# print(pd.Series(5, index=index))


# s = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
# print(f'Pick one element: {s["a"]}')
# print(f'Pick a few elements: {s[["a", "b"]]}')
# print(f'Slicing: {s[:2]}')
# print(f'Element-wise summation: {s + s}')


# s = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
# print(f'Filtering: {s[s > 2]}')


# s = pd.Series(np.arange(3), index=['a', 'b', 'c'])
# s.name = 'Data'
# s.index.name = 'Index'
# print(s)


# students_marks_dict = {"student": ["Студент_1", "Студент_2", "Студент_3"],
#                        "math": [5, 3, 4],
#                        "physics": [4, 5, 5]}
# students = pd.DataFrame(students_marks_dict)
# print(students)
# print(students.index)
# print(students.columns)
# students.index = ['A', 'B', 'C']
# print(students)
# print(students.loc['B':])
# print(type(students['student']))


filepath = '6-2-pandas/data/Students_Performance_132b1e1ff9.csv'
data = pd.read_csv(filepath)

# print(data.head(10))
# print(data.tail(3))
# print(data[5:10])

# print(data[data[data.columns[0]] == 'female'])
# print(data[data['test preparation course'] == 'completed']['math score'].head(5))

# with_course = data[data['test preparation course'] == 'completed']

# print(with_course[['math score',
#                    'reading score',
#                    'writing score']].sort_values(['math score', 
#                                                  'reading score', 
#                                                  'writing score'], ascending=False).head())

# data['total score'] = data['math score'] + data['reading score'] + data['writing score']
# with_course = data[data['test preparation course'] == 'completed']
# print(with_course.head())
# print(with_course.sort_values(['total score'], ascending=False).head())

# scores = data.assign(total_score = lambda x: data['math score'] + data['reading score'] + data['writing score'])
# print(scores.head())
# print(scores.sort_values(['total_score'], ascending=False).head())

# print(data.groupby(['gender', 'test preparation course'])['writing score'].count())

# agg_functions = {'math score': ['mean', 'median']}
# print(data.groupby(['gender', 'test preparation course']).agg(agg_functions))

# plt.hist(data['math score'], label='Math test')
# plt.xlabel('Math scores')
# plt.ylabel('Students')
# plt.legend()
# plt.show()
