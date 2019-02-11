#Backslash on Windows and Forward Slash on OS X and Linux

import os

os.path.join('usr', 'bin', 'spam')

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))
