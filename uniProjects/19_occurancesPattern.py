# find all occurances of a pattern in a string using regexp

import re

# Input string
text = input("Enter a string: ")

# Input pattern to search (regex) #\w+   \".*?\"
pattern = input("Enter the regex pattern: ")

# Find all occurrences of the pattern
matches = re.findall(pattern, text)

# Check if matches are found
if matches:
    print("Matches found:", matches)
else:
    print("No matches found.")
