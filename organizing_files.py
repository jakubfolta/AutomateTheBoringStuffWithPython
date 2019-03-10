import shutil
import os

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
shutil.rmtree('C:\\New folder')
