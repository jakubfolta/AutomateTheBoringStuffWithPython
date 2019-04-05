#! python3

'''backup_zip-solidifying.py - Copies an entire folder and its contents into
 a ZIP file whose filename increments.'''

# Import essential modules.
import os
import zipfile

# Set directory to backup.
dir_to_backup = r'C:\Users\ogi-8\Desktop\PythonProjects\AddDigits'
dir_basename = os.path.basename(dir_to_backup)

# Walk through directory with for loop and os.walk().
for file in os.walk(dir_to_check):

# Set new filename for backup.
    num = 1
    while True:
        zip_filename = dir_basename + '_' + str(num) + '.zip'
        if not os.path.exists(zip_filename):
            break
        num +=1

# TODO: Create zip file.


# TODO: Backup folder and files.
