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

# TODO: Create new filename.
    num = 1
    while True:
        zip_name = base_name + '_' + str(num) + '.zip'
        if not os.path.exists(zip_name):
            break
        num += 1


# TODO: Create zipfile.
# TODO: Walk through directory tree in for loop.
# TODO: Add folder to zipfile.
# TODO: Add files to zipfile.
# TODO: Close zipfile.

create_zipfile(r'C:\Users\ogi-8\Desktop\PythonProjects\AddDigits\Sample_zip')
