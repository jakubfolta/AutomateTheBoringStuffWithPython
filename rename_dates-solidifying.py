#! python3

# rename_dates.py - Rename filenames with american date format to european date format.

# Import essential modules.
import os
import re
import shutil

# TODO: Create date format regex.
date_pattern = re.compile(r'''^(.*?) # all text before date
    ((0|1)?\d)-                       # one or two digits for a month
    ((0|1|2|3)?\d)-                   # one or two digits for a day
    ((19|20)\d\d)                    # four digits for a year
    (.*?)$
''', re.VERBOSE)

# Loop the files in the working directory.
for amer_filename in os.listdir('.'):
    match = date_pattern.search(amer_filename)

# Skip files without match to regex.
    if match == None:
        continue

# Get needed part of filename.
    before_date = match.group(1)
    month = match.group(2)
    day = match.group(4)
    year = match.group(6)
    after_date = match.group(8)

# Create proper filename.
    europ_filename = before_date + day + '-' + month + '-' + year + after_date

# Get absolut paths to exchange.
    abs_path = os.path.abspath('.')
    amer_filename = os.path.join(abs_path, amer_filename)
    europ_filename = os.path.join(abs_path, europ_filename)

# Exchange filenames and print changes to console.
    print('Change "{}" to "{}"'.format(amer_filename, europ_filename))
    shutil.move(amer_filename, europ_filename)
