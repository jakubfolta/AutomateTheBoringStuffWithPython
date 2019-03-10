import shutil
import os
import send2trash

os.chdir('C:\\')
#shutil.copy('C:\\BnetLog.txt', 'C:\\delicious')
#shutil.copy('C:\\BnetLog.txt', 'C:\\delicious\spam.txt')

# shutil.copytree('C:\\New folder', 'C:\\New folder backup')
#
# shutil.move('C:\\BnetLog.txt', 'C:\\New folder backup2')
# shutil.move('C:\\New folder backup2', 'C:\\backup')

# Permanently deleting files and folders
#os.unlink('C:\\backup')
#os.rmdir('C:\\New f')
#shutil.rmtree('C:\\New folder')
os.chdir('C:\\Users\ogi-8\Desktop\PythonProjects')
with open('file.txt', 'a') as bacon_file:
    bacon_file.write('Bacon isn\'t a vegetable.')

send2trash.send2trash('file.txt')
