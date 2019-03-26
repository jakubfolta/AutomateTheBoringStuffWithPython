#! python3

# backup_zip-solidifying.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile
import os

# Create function.
def create_zipfile(folder):

# Create abspath for folder path.
    folder = os.path.abspath(folder)

# Create zipfile name.
    number = 1
    while True:
        zip_name = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_name):
            break
        number += 1

# Create zipfile.
    print('Creating {}'.format(zip_name))
    zip_file = zipfile.ZipFile(zip_name, 'w')

# Loop through pathtree and add to zipfile folders and files.
    for folder, subfolder, filename in os.walk(folder):

# Add folder to zip_file.
        print('Adding files in {}.'.format(folder))
        zip_file.write(folder)

# Add files.
        for file in filename:
            base_name = os.path.basename(folder) + '_'
            if file.startswith(base_name) and file.endswith('.zip'):
                continue
                zip_file.write(os.path.join(folder, file))
    zip_file.close()
    print('Done')

create_zipfile(r'C:\Users\ogi-8\Desktop\PythonProjects\AddDigits')
