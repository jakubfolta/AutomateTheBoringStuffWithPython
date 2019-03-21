#! python3

# zip_file-solid.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

# Import essential modules.
import os
import zipfile

# Create function and set abspath to function argument.
def create_backup(folder):
    abspath = os.path.abspath(folder)

# Create a zipfile name using while loop.
    zip_number = 1
    while True:
        zip_name = os.path.basename(folder) + '_' + str(zip_number) + '.zip'
        if not os.path.exists(zip_name):
            break
        zip_number += 1

# Create a zipfile and its filemode.
    print('Creating zipfile named {}'.format(zip_name))
    zip_file = zipfile.ZipFile(zip_name, 'w')

# Use for loop and os.walk to add folders and its files to zipfile.
    for folder,subfolders, files in os.walk(folder):
        base_name = os.path.basename(folder) + '_'
        print('Adding files in {}'.format(folder))
        zip_file.write(folder)
        for file in files:
            if file.startswith(base_name) and file.endswith('.zip'):
                continue
            zip_file.write()



# TODO: Close zipfile.
# TODO: Call function.
