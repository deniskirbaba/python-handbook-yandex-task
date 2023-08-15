def merge(t1, t2):
    result = []
    i_t1 = 0
    i_t2 = 0
    for i in range(len(t1) + len(t2)):
        if i_t1 == len(t1):
            result.extend(t2[i_t2:])
            break
        elif i_t2 == len(t2):
            result.extend(t1[i_t1:])
            break
        if t1[i_t1] <= t2[i_t2]:
            result.append(t1[i_t1])
            i_t1 += 1
        else:
            result.append(t2[i_t2])
            i_t2 += 1
    return tuple(result)


print(merge((7, 12), (1, 9, 50)))
