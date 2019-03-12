#! python3

# rename_dates.py - Rename filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.

import os
import re
import shutil

# Create regex to find files with American date format.
date_pattern = re.compile(r'''^(.*?) # all text before the date
    ((0|1)?\d)-                      # one or two digits for the month
    ((0|1|2|3)?\d)-                  # one or two for day
    ((19|20)\d\d)                    # four digits for year
    (.*?)$                           # all text after the date
''', re.VERBOSE)

# TODO: Loop over the files in the working directory.
for amer_filename in os.listdir('.'):
    mo = date_pattern.search(amer_filename)

# TODO: Skip files without date.
    if mo == None:
        continue

# TODO: Get the different parts of the filename.
    befor_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(3)
    year_part = mo.group(4)
    after_part = mo.group(5)

# TODO: Form the European-style filename.

# TODO: Get the full, absolute file paths.

# TODO: Rename the files.
