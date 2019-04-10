#! python3

'''rename-date-format-solidifying.py - Rename filenames with american date format to european date format.'''

# Import essential modules.
import os
import re
import shutil

# Create american date format regex.
amer_date_format = re.compile(r'''^(.*?)    # all text before date
    ((0|1)?\d)-                             # one or two digits for a month
    ((0|1|2|3)?\d)-                         # one or two digits for a day
    ((19|20)\d\d)                           # four digits for a year
    (.*?)$                                  # all text after date
''', re.VERBOSE)

# Set directory to check.
dir_to_check = r'C:\Users\ogi-8\Desktop\PythonProjects\AutomateTheBoringStuffWithPython'

# Create for loop and use os.listdir() to check files inside directory.
for file in os.listdir(dir_to_check):
    match = amer_date_format.search(file)
    if match == None:
        continue

# Get groups from matches.
    before_date = match.group(1)
    month = match.group(2)
    day = match.group(4)
    year = match.group(6)
    after_date = match.group(8)

# Create european date format from matched groups.
    europ_filename = before_date + day + '-' + month + '-' + year + after_date

# Set proper absolute paths to exchange.
    europ_filename_abspath = os.path.join(dir_to_check, europ_filename)
    amer_filename_abspath = os.path.join(dir_to_check, file)

# Print and change the filename using shutil module.
    print('Change this filename "{}"\nto this\n"{}"'.format(amer_filename_abspath, europ_filename_abspath))
    #shutil.move(amer_filename_abspath, europ_filename_abspath)
