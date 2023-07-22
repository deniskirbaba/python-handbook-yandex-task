def make_linear(data, level=1):
    global new_data
    if 'new_data' not in globals():
        new_data = []
    
    for element in data:
        if isinstance(element, list):
            make_linear(element, level + 1)
        else:
            new_data.append(element)
    if level == 1:
        return new_data
    

result = make_linear([1, [2, [3, 4]], 5, 6])
print(result)
