try:
    func('dsaf', 34)
except ArithmeticError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print('No errors.')


# try:
#     func(1, 4)
#     func('asdfjkl', 'asdf')
#     func(2, 'fdas')
#     func(True, 'sdaf')
#     func(print, print)
# except Exception as e:
#     print(e)