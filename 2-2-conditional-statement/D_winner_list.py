dist = 43872

p_speed = float(input())
v_speed = float(input())
t_speed = float(input())

if p_speed > v_speed:
    if t_speed > p_speed:
        print("1. Толя\n2. Петя\n3. Вася")
    elif t_speed > v_speed:
        print("1. Петя\n2. Толя\n3. Вася")
    else:
        print("1. Петя\n2. Вася\n3. Толя")
elif t_speed > v_speed:
    print("1. Толя\n2. Вася\n3. Петя")
elif t_speed > p_speed:
    print("1. Вася\n2. Толя\n3. Петя")
else:
    print("1. Вася\n2. Петя\n3. Толя")
