#! python3

# zip-drill_up.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

# Import essential modules.
import os
import zipfile

# Create a function and set abs path to argument.
def create_backup(folder):
    abspath_folder = os.path.abspath(folder)

# Create zip file name in a while loop.
    zip_number = 1
    while True:
        zip_name = os.path.basename(abspath_folder) + '_' + str(zip_number) + '.zip'
        if not os.path.exists(zip_name):
            break
        zip_number += 1

# Create zip file and set filemode.
    print('Creating zip file named {}'.format(zip_name))
    zip_file = zipfile.ZipFile(zip_name, 'w')       # Don't forget about filemode!!!

# Loop through argument path and add folders and files to zip file.
    for folder, subfolders, files in os.walk(folder):
        folder_base = os.path.basename(folder) + '_'
        print('Adding files in {}.'.format(folder))
        zip_file.write(folder)
        for file in files:
            if file.startswith(folder_base) and file.endswith('.zip'):
                continue
            zip_file.write(os.path.join(folder, file))

# Close zip file.
    zip_file.close()
    print('Done.')

# Call function.
create_backup('C:\\Users\ogi-8\Desktop\PythonProjects\AutomateTheBoringStuffWithPython\zip_test')
