sides_squared_asc = sorted([float(input())**2 for i in range(3)])

if sides_squared_asc[2] < (sides_squared_asc[0] + sides_squared_asc[1]):
    print('крайне мала')
elif sides_squared_asc[2] > (sides_squared_asc[0] + sides_squared_asc[1]):
    print('велика')
else:
    print('100%')