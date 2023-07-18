def modern_print(s):
    if 'msgs' not in globals(): 
        global msgs
        msgs = []
    
    if s not in msgs:
        print(s)
        msgs.append(s)


modern_print('hello')
modern_print('hello')
modern_print('asd')
modern_print('asd')
