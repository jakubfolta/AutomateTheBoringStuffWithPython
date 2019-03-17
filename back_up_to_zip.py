#! python3

# back_up_to_zip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile
import os

# Backup the entire contents of "folder" into a zip file.
def backup_to_zip(folder):
    folder = os.path.abspath(folder)
    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1

    # Create the zip file.
    print('Creating "{}"'.format(zip_filename))
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for folder_name, subfolders, file_names in os.walk(folder):
        # Add the curent folder to zip file.
        print('Adding files in {}...'.format(folder_name))
        backup_zip.write(folder_name)
        # Add all the files in this folder to the zip file.
        for filename in file_names:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            backup_zip.write(os.path.join(folder_name, filename))
    backup_zip.close()

    print('Done')

backup_to_zip('PythonProjects\\AutomateTheBoringStuffWithPython')
