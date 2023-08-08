import numpy as np

# a = np.array([1, 2, 3, 4])
# b = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
# print(f"a[0] = {a[0]}")
# print(f"b[0] = {b[0]}")


# a = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
# print(f"a.ndim = {a.ndim}, a.shape = {a.shape}, a.size = {a.size}, a.dtype = {a.dtype}, a.itemsize = {a.itemsize}")


# a = np.array([1, 2, 3], dtype=np.uint8)
# a[0] = 256
# print(a)


# a = np.array([1, 2.5, 3])
# print(a)
# print(a.dtype)
# b = np.array(['text', 1, 2.5])
# print(b)
# print(b.dtype)


# a = np.zeros((4, 3))
# print(a)
# print()
# a = np.zeros((4, 3), dtype="int32")
# print(a)


# a = np.arange(1, 10)
# print(a)
# print()
# a = np.arange(1, 5, 0.4)
# print(a)


# a = np.linspace(1, 5, 10)  # задаётся начало, конец диапазона и количество значений
# print(a)


# a = np.zeros((4, 3), dtype="uint8")
# print(a)
# print()
# a = a.reshape((2, 6))
# print(a)


# a = np.zeros((4, 3), dtype="uint8")
# print(a)
# print()
# a.resize((2, 2, 3))
# print(a)


# a = np.zeros((4, 3), dtype="uint8")
# print(a)
# print()
# a = a.reshape((2, 3, -1))
# print(a)


# a = np.array([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]])
# b = np.array([[0, 0, 1],
#               [0, 1, 0],
#               [1, 0, 0]])
# print(a @ b)


# a = np.arange(1, 13).reshape(4, 3)
# print(a)
# print("Транспонирование")
# print(a.transpose())
# print("Поворот вправо")
# print(np.rot90(a))
# print("Поворот влево")
# print(np.rot90(a, -1))


# a = np.array([[1, 2, 3],
#              [4, 5, 6],
#              [7, 8, 9]])
# print(a.sum())
# print(a.min())
# print(a.max())


# a = np.array([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]])
# print(a.sum(axis=0))  # сумма чисел в каждом столбце
# print(a.sum(axis=1))  # сумма чисел в каждой строке
# print(a.min(axis=0))  # минимум по столбцам
# print(a.max(axis=1))  # максимум по строкам


# a = np.arange(1, 13).reshape(3, 4)
# print(a)
# print()
# print(a[:2, 2:])
# print()
# print(a[:, ::2])


# a = np.arange(1, 13).reshape(3, 4)
# print(a)
# for row in a:
#     print(row)


# a = np.arange(1, 13).reshape(3, 4)
# print(a)
# print()
# print("; ".join(str(el) for el in a.flat))
