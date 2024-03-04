def is_palindrome(obj) -> bool:
    '''
    Takes the integer, string, tuple or list and check if this object is palindrome.

            Parameters:
                    obj (int, string, tuple, list): An object to be checked
            
            Returns:
                    res (bool): Boolean value (True is palindrome and False otherwise)
    '''
    if isinstance(obj, int):
        obj = str(obj)
    length_obj = len(obj)
    res = obj[:length_obj // 2] == obj[(length_obj + 1) // 2:][::-1]
    return res

str_tests = ['', 'q', 'qq', 'qa', 'qaq', 'qaa']
str_tests_answers = [True, True, True, False, True, False]
assert [is_palindrome(i) for i in str_tests] == str_tests_answers, f'string tests failed'

