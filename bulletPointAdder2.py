#! python3
#Another mothod.

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')

for x in range(len(lines)):
    lines[x] = '* ' + lines[x]

lines = '\n'.join(lines)
print(lines)

pyperclip.copy(lines)
