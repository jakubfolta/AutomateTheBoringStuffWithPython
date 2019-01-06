spam = ['apples', 'bananas', 'tofu', 'cats']

def convertListToString(argument):
    convertedArgument = ''
    for x in argument:
        if x == argument[len(argument) - 1]:
            convertedArgument += 'and ' + x
        else:
            convertedArgument += x + ', '
    
    print(convertedArgument)

convertListToString(spam)

    
