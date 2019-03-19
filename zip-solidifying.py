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
        zip_name = os.path.basename(abspath) + '_' + '.zip'
        if not os.path.exists(zip_name):
            break
        number += 1

# TODO: Create zipfile.
# TODO: Use for loop and os.walk() to add current folder and its files to zipfile.
# TODO: Close zipfile.
# TODO: Call function.
