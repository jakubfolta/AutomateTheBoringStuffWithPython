#! python3

# zip-drill_up.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

# Create a function and set abs path to argument.
def create_backup(folder):
    abspath_folder = os.path.abspath(folder)

# Create zip file name in a while loop.
    zip_number = 1
    while True:
        zip_name = os.path.basename(abspath_folder) + '_' + str(zip_number) + '.zip'
        if not os.path.exists(zip_name):
            break
        number += 1

# Create zip file.
    print('Creating zip file named {}'.format(zip_name))
    zip_file = zipfile.ZipFile(zip_name)

# TODO: Loop through argument path and add folders and files to zip file.
    for folder, subfolders, files in os.walk(folder):
        folder_base = os
        print('Adding files in {}.'.format(folder))
        zip_file.write(folder)
        for file in files:
            zip_file.write()

# TODO: Close zip file.
# TODO: Call function.
