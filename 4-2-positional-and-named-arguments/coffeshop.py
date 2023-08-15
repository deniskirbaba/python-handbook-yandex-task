def isavailable(drink):
    match drink:
        case 'Эспрессо':
            if in_stock['coffee'] > 0:
                in_stock['coffee'] -= 1
                return True
        case 'Капучино':
            if in_stock['coffee'] > 0 and in_stock['milk'] > 2:
                in_stock['coffee'] -= 1
                in_stock['milk'] -= 3
                return True
        case 'Макиато':
            if in_stock['coffee'] > 1 and in_stock['milk'] > 0:
                in_stock['coffee'] -= 2
                in_stock['milk'] -= 1
                return True
        case 'Кофе по-венски':
            if in_stock['coffee'] > 0 and in_stock['cream'] > 1:
                in_stock['coffee'] -= 1
                in_stock['cream'] -= 2
                return True
        case 'Латте Макиато':
            if in_stock['coffee'] > 0 and in_stock['milk'] > 1 and in_stock['cream'] > 0:
                in_stock['coffee'] -= 1
                in_stock['milk'] -= 2
                in_stock['cream'] -= 1
                return True
        case 'Кон Панна':
            if in_stock['coffee'] > 0 and in_stock['cream'] > 0:
                in_stock['coffee'] -= 1
                in_stock['cream'] -= 1
                return True
        case _:
            return False


def order(*args):
    for drink in args:
        if isavailable(drink):
            return drink
    return 'К сожалению, не можем предложить Вам напиток'


in_stock = {"coffee": 4, "milk": 4, "cream": 0}
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))

'''
Эспрессо готовится из: 1 порции кофейных зерен.
Капучино готовится из: 1 порции кофейных зерен и 3 порций молока.
Макиато готовится из: 2 порций кофейных зерен и 1 порции молока.
Кофе по-венски готовится из: 1 порции кофейных зерен и 2 порций взбитых сливок.
Латте Макиато готовится из: 1 порции кофейных зерен, 2 порций молока и 1 порции взбитых сливок.
Кон Панна готовится из: 1 порции кофейных зерен и 1 порции взбитых сливок.
'''