def spam():
    bacon()
def bacon():
    raise Exception('This is an exception!')


import traceback
try:
    raise Exception('This is the error message!')
except:
    with open('error_info.txt', 'w') as error_file:
        error_file.write(traceback.format_exc())
    print('The traceback info was written to error_info.txt')
