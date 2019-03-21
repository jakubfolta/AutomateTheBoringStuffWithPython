#! python3

# ren_dates-solidifying.py - program which change filenames with european date format to american date format.

# Import modules.
import os
import re
import shutil

# Create regex to find european date format.
date_pattern = re.compile(r'''^(.*?)  # all text before date
    ((0|1|2|3)?\d)-                   # one or two digits for a day
    ((0|1)?\d)-                       # one or two digits for a month
    ((19|20)\d\d)                     # four digits for a year
    (.*?)$                            # all text after the date
''', re.VERBOSE)

# Loop the files in the working directory.
for europ_filename in os.listdir('.'):
    match = date_pattern.search(europ_filename)

# Skip files without dates.
    if match == None:
        continue

# Select parts of the date.
    before_text = match.group(1)
    day_match = match.group(2)
    month_match = match.group(4)
    year_match = match.group(6)
    after_text = match.group(8)

# Create proper filename.
    amer_filename = before_text + month_match + '-' + day_match + '-' + year_match + after_text

# Create absolute paths to exchange.
    abs_path = os.path.abspath('.')
    europ_filename = os.path.join(abs_path, europ_filename)
    amer_filename = os.path.join(abs_path, amer_filename)

# Change filenames and print changes.
    print('Change "{}" to "{}"'.format(europ_filename, amer_filename))
    shutil.move(europ_filename, amer_filename)
