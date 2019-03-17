#! python3

# back_up_to_zip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile
import os

def backup_to_zip(folder):
    # Backup the entire contents of "folder" into a zip file.
    folder = os.path.abspath(folder)
    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1
        
