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

# TODO: Set directory to check.


# TODO: Create for loop and use os.listdir() to check files inside directory.
# TODO: Get groups from matches.
# TODO: Create european date format from matched groups.
# TODO: Set proper absolute paths to exchange.
# TODO: Print and change the filename using shutil module.
