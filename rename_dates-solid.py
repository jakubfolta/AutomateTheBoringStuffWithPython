#! python3

# rename_dates-solid.py - program which change filenames with european date format to american date format.

# Import essential modules.
import os
import re
import shutil

# Create regex to find european date format.
europ_date_regex = re.compile(r'''^(.*?)    # all text before date
    ((0|1|2|3)?\d)-                         # one or two digits for day
    ((0|1)?\d)-                             # one or two digits for month
    ((19|20)\d\d)                           # four digits for year
    (.*?)$                                  # all text after date
''', re.VERBOSE)

# Loop through files in given directory and select groups of the match.
for file in os.listdir('.'):
    match = europ_date_regex.search(file)
    if match = None:
        continue

    before_date = match.group(1)
    day = match.group(2)
    month = match.group(4)
    year = match.group(6)
    after_date = match.group(8)

# Create new american date format.
    american_filename = before_date + month + '-' + day + '-' + year + after_date

# Set american and european file paths.
    abs_path = os.path.abspath('.')
    europ_filename = os.path.join(abs_path, file)
    amer_filename = os.path.join(abs_path, american_filename)

# Exchange filenames
    print('Exchange {} to {}'.format(europ_filename, amer_filename))
    # shutil.move(europ_filename, amer_filename)
