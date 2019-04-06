#! python3

'''zip_file-solidifying.py - Copies an entire folder and its contents into
 a ZIP file whose filename increments.'''

# Import essential modules.
import os
import zipfile

# Create function.
def create_zipfile(directory):

# Create basename.
    base_name = os.path.basename(directory)

# Create new filename.
    num = 1
    while True:
        zip_name = base_name + '_' + str(num) + '.zip'
        if not os.path.exists(zip_name):
            break
        num += 1

# Create zipfile.
    print('Creating "{}"'.format(zip_name))
    zip_file = zipfile.ZipFile(zip_name, 'w')

# Walk through directory tree in for loop.
    for folder, subfolder, files in os.walk(directory):

# Add folder to zipfile.
        if files:
            print('Adding files in "{}"'.format(folder))
            zip_file.write(folder)
            print('Adding:')

# Add files to zipfile.
            for file in files:
                if file.endswith('.zip'):
                    continue
                print(file)

# Close zipfile.
    else:
        print('Backup completed!')
    zip_file.close()

create_zipfile(r'C:\Users\ogi-8\Desktop\PythonProjects\AddDigits\Sample_zip')
