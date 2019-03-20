#! python3

# zip-solidifying.py -  Copies an entire folder and its contents into
# a ZIP file whose filename increments.


# Import essential modules.
import os
import zipfile

# Create function.
def backup_folder(folder):
# Set abspath to variable.
    abspath = os.path.abspath(folder)

# Create zipfile name with while loop.
    number = 1
    while True:
        zip_name = os.path.basename(abspath) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_name):
            break
        number += 1

# Create zipfile.
    print('Creating {}'.format(zip_name))
    zip_file = zipfile.ZipFile(zip_name, 'w')

# Use for loop and os.walk() to add current folder and its files to zipfile.
    for folder, subfolder, filename in os.walk(folder):
        print('Adding files in {} folder.'.format(folder))
        zip_file.write(folder)
        for file in filename:
            abspath = os.path.basename(folder) + '_'
            if file.startswith(abspath) and file.endswith('.zip'):
                continue
            zip_file.write(os.path.join(file))
    zip_file.close()

# Close zipfile.
    print('Done')

# Call function.
backup_folder('C:\\Users\ogi-8\Desktop\PythonProjects\AutomateTheBoringStuffWithPython\zip_test')
