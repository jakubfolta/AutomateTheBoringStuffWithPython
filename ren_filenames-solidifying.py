#! python3

'''ren_filenames-solidifying.py - Rename filenames with american date format to european date format.'''

# Import essential modules.
import shutil
import os
import re

# Create directory to check.
dir_to_check = r'C:\Users\ogi-8\Desktop\PythonProjects\AutomateTheBoringStuffWithPython'

# Create date format regex.
amer_format_regex = re.compile(r'''^(.*?)     # all text before date
    ((0|1)?\d)                                # one or two digits for a month
    ((0|1|2|3)?\d)                            # one or two digits for a day
    ((19|20)\d\d)                             # four digits for a year
    (.*?)$                                    # all text after date
''', re.VERBOSE)

# Loop through files in specified directory with os.listdir().
for file in os.listdir(dir_to_check):
    match = amer_format_regex.search(file)
    if match == None:
        continue

# Set matched groups.
    before_date = match.group(1)
    month = match.group(2)
    day = match.group(4)
    year = match.group(6)
    after_date = match.group(8)

# Set abs paths to old and new filename.
europ_filename = before_date + day + month + year + after_date
amer_filename_abs = os.path.join(dir_to_check, file)
europ_date_abs = os.path.join(dir_to_check, europ_filename)

# TODO: Change filename to proper date format.
print('Change this "{}" filename to this "{}"'.format(amer_filename_abs, europ_date_abs))
shutil.move
# TODO:
