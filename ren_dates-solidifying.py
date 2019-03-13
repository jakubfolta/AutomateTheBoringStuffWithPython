#! python3

# ren_dates-solidifying.py - program which change filenames with european date format to american date format.

# TODO: Import modules.
import os
import re
import shutile

# TODO: Create regex to find european date format.
european_date = re.compile(r'''^(.*?) # all text before date
    ((0|1|2|3)?\d)-                   # one or two digits for a day
    ((0|1)?\d)-                       # one or two digits for a month
    ((19|20)\d\d)                     # four digits for a year
    (.*?)$                            # all text after the date
''', re.VERBOSE)

# TODO: Loop the files in the working directory.
for europ_filename in os.listdir('.'):
    

# TODO: Skip files without dates.
# TODO: Select parts of the date.
# TODO: Create proper filename.
# TODO: Create absolute paths to exchange.
# TODO: Change filenames and print changes.
