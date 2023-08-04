# print(";".join(str(1 / x) for x in range(int(input()), int(input()) + 1)))


# interval = range(int(input()), int(input()) + 1)

# if 0 in interval:
#     print('Zero in interval.')
# else:
#     print(';'.join((str(1 / n) for n in interval)))


# start = input()
# end = input()
# if not (start.lstrip('-').isdigit() and end.lstrip('-').isdigit()):
#     print('Start and end of interval should be numbers.')
# else:
#     interval = range(int(start), int(end) + 1)
#     if 0 in interval:
#         print('Zero in interval.')
#     else:
#         print(';'.join(str(1 / n) for n in interval))


# eception syntax
#
# try:
#   <code, which can call the exception during the execution>
# except <exceptionclass_1>:
#   <exceptionclass_1 processing code>
# except <exceptionclass_2>:
#   <exceptionclass_2 processing code>
# ...
# else: 
#   <this code executes if no exceptions triggered>
# finally:
#   <this code executed always>


# try:   
#     print(';'.join((str(1 / n) for n in range(int(input()), int(input()) + 1))))
# except ZeroDivisionError:
#     print('Zero in interval.')
# except ValueError:
#     print('Start and end of interval should be numbers.')
# except Exception:
#     print('Unknown error.')
# else:
#     print('Success.')
# finally:
#     print('End of program.')


# raise ValueError('Value error raising example.')


