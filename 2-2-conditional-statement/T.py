strings = [input() for i in range(3)]
strings_with_hare = [i for i in strings if 'зайка' in i]
res_string = min(strings_with_hare)
print(res_string, len(res_string))