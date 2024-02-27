n_max = int(input())

layers = ['1']

width = 1
n_layers = 1
cur_value = 1

while n_max - cur_value > 0:
    n_layers += 1
    end_of_layer_value = min(n_max, cur_value + n_layers)
    
    cur_layer = ' '.join([str(i) for i in range(cur_value + 1, end_of_layer_value + 1)])
    layers.append(cur_layer)
    width = max(width, len(cur_layer))
    
    cur_value += n_layers

for i in range(n_layers):
    print(f'{layers[i]: ^{width}}')