import shutil
import os

os.chdir('C:\\')
shutil.copy('C:\\BnetLog.txt', 'C:\\delicious')
shutil.copy('C:\\BnetLog.txt', 'C:\\delicious\spam.txt')
