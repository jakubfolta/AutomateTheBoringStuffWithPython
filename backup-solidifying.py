#! python3

'''backup_zip-solidifying.py - Copies an entire folder and its contents into
 a ZIP file whose filename increments.'''

# Import essential modules.
import os
import zipfile

# Create function.
def create_zipfile(directory):

# Set directory to backup.
    dir_basename = os.path.basename(directory)

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


# Walk through directory with for loop and os.walk().
    for folder, subfolder, files in os.walk(directory):
        folder_base = os.path.basename(folder)

# Backup folder.
        print('Adding files in "{}"'.format(folder_base))
        zip_file.write(folder)
# Backup files.
        for file in files:
            if file.endswith('.zip'):
                continue
            print('Adding file: "{}"'.format(file))
            zip_file.write(os.path.join(folder, file))
    else:
        print('Backup complete!')
    zip_file.close()

create_zipfile(r'C:\Users\ogi-8\Desktop\PythonProjects\AddDigits')
