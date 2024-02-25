# print(ord('w'), ord('t'))
# print(chr(116), chr(119))

color = input()
match color:
    case 'red' | 'yellow':
        print('Stop')
    case 'green':
        print('Go')
    case _:
        print('Incorrect color')