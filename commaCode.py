spam = ['apples', 'bananas', 5, 'tofu', [3, 4], 'cats', 2]

def convertListToString(argument):
    convertedArgument = ''

    for x in argument:
        if x == argument[len(argument) - 1]:
            convertedArgument += 'and ' + str(x)
        else:
            convertedArgument += str(x) + ', '
    return convertedArgument

print(convertListToString(spam))


def convertListToString(argument):
    phrase = ''

    for x in argument:
        if x == argument[len(argument) - 1]:
            phrase += 'and' + str(x) + '.'
        else:
            phrase += str(x) + ', '
    return phrase

print(convertListToString(spam))

    
