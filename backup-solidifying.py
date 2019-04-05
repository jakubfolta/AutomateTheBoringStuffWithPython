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
for folder, subfolder, files in os.walk(dir_to_check):
    folder_base = os.path.basename(folder)
    
# Set new filename for backup.
    num = 1
    while True:
        zip_filename = dir_basename + '_' + str(num) + '.zip'
        if not os.path.exists(zip_filename):
            break
        num +=1

# Create zip file.
    print('Creating zip file: "{}"'.format(zip_filename))
    zip_file = zipfile.ZipFile(zip_filename, 'w')

# TODO: Backup folder and files.
    print('Adding files in "{}"'.format(folder_base))
    zip_file.write(folder)
    for file in files:
        if not
