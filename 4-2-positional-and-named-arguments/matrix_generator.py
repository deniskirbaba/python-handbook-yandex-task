def make_matrix(size, value=0):
    if isinstance(size, int):
        return [[value for j in range(size)] for i in range(size)]
    return [[value for j in range(size[0])] for i in range(size[1])]


print(make_matrix((2, 4), 7))
