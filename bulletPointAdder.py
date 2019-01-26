#! python3
#bulletPointAdder.py - Adds Wikipedia bullet points to the start
#of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()
print(text)
text = text.split('\n')
print(text)
modifiedText = ''

#Seperate lines and add stars.

for x in text:
    if x == text[len(text) - 1]:
        modifiedText += '* ' + x
    else:
        modifiedText += '* ' + x + '\n' 
print(modifiedText)
    
pyperclip.copy(modifiedText)
