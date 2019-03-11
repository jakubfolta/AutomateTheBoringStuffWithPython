#! python3

# rename_dates.py - Rename filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.

import os
import re
import shutil

# TODO: Create regex to find files with American date format.
date_pattern = re.compile(r'''^(.*?) # all text before the date
    ((0|1)?\d)-                      # one or two digits for the month
    ((0|1|2|3)?\d)-                  # one or two for day
    ((19|20)\d\d)                    # four digits for year
    (.*?)$                           # all text after the date
''', re.VERBOSE)

# TODO: Loop over the files in the working directoryself.

# TODO: Skip files without date.

# TODO: Get the different parts of the filename.

# TODO: Form the European-style filename.

# TODO: Get the full, absolute file paths.

# TODO: Rename the files.
