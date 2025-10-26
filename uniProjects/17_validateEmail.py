# validate email address using regular expression

"""
^ → Start of the string.
[a-zA-Z0-9._%+-]+ → Matches the username (letters, numbers, and allowed special characters).
@ → Must contain exactly one @ symbol.
[a-zA-Z0-9.-]+ → Domain name (letters, numbers, dots, and hyphens).
\. → Literal dot before the domain extension.
[a-zA-Z]{2,} → Top-level domain (like .com, .org, at least 2 characters).
$ → Use this to ensure whole string is matched.
"""
import re

# Regular expression pattern for validating an email
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
def validate_email(email):
    if re.match(email_pattern, email):
        return True
    else:
        return False

# Test examples
emails = ["example@gmail.com", "user.name@domain.co", "invalid-email@", "user@.com"]

for e in emails:
    if validate_email(e):
        print(f"{e} is valid.")
    else:
        print(f"{e} is invalid.")
