""" 
Regular expressions are a powerful pattern-matching language used to:
  Search text
  Match specific patterns (like phone numbers, emails, dates)
  Validate inputs
  Extract parts of a string
  Replace text based on patterns


  Function	    Purpose
  re.search()	Finds the first match in the string
  re.match()	Checks for a match at the beginning of the string
  re.findall()	Returns all matches in a list
  re.sub()	    Replaces text using regex
  re.split()	Splits a string by regex pattern
  
match.group() → extracts the exact substring that matched the pattern.


  regex patterns
1)PHONE NUMBER:  r'\+\d{1,3}\d{4}-\d{6}'
2)EMAIL ADDRESS: r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
3)WEBSITE URL  : r'https?://(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
4)DD:MM:YYYY   : r'\b\d{2}-\d{2}-\d{4}\b'
5)HH:MM 24 hr  : r'\b([01]\d|2[0-3]):[0-5]\d\b'
6)POSTAL CODE  : r'\b\d{6}\b'
7)USERNAME     : r'^[a-zA-Z0-9_]{3,15}$'
8)PASSWORD     : r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
9)EXTRACT HASH : r'#\w+'
10) Find quoted txt: r'\".*?\"'



? : Means a quantifier, it says preceeding thing is optional | (www\.)?: www. is optional, https?: s is opti
[....] : square brackets means anything characters which are in these: [abc] One of the characters a, b, or c
(abc) : The exact sequence “abc”
    -\d{1,3} → 1 to 3 digits (country code, e.g., 91)
    -\d{4} → exactly 4 digits (part of the local number)
    -\d{6} → exactly 6 digits (subscriber number)
    -\d matches any digit 0–9


    lookahead means scan what comes after : ?=.*[A-Z] --> means whatever is in braces scan A-Z, if met condition then true
(?=) - positive lookahead
(?!) - negative lookahead
(?<=) - positive lookbehind
(?<!) - negative lookbehind
(?>) - atomic group
    Find expression A where expression B follows: A(?=B)
    Find expression A where expression B does not follow: A(?!B)
    Find expression A where expression B precedes: (?<=B)A
    Find expression A where expression B does not precede: (?<!B)A
    \d(?=\sUSD) matches a digit before " USD"

\. consider . as literal dot, i.e., an actual . character in the text npt any symbol or operator.
"""
import re
def website():
    
    text = "Visit https://www.variabletribe.com for more."
    pattern = r'https?://(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    match = re.search(pattern, text)
    print(match.group() if match else "No match")
# website()

def email():

    text = "Contact me at farhan123@gmail.com"
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    match = re.search(pattern, text)
    print(match.group() if match else "No match")
# email()

def phone():
    text = "+919045-356778"
    pattern = r'\+\d{1,3}\d{4}-\d{6}'

    match = re.search(pattern, text)
    print(match.group() if match else "No match")
# phone()

def date():
    text = "Today's date is 13-10-2025."
    pattern = r'\b\d{2}-\d{2}-\d{4}\b'
    # \b ensures your pattern is treated as a “whole word” or token,” not part of a longer string.
        # \b matches positions, not characters.
        # At start: must be non-word → word
        # At end: must be word → non-word

    match = re.search(pattern, text)
    print(match.group() if match else "No match")
# date()

def time():
    text = "The meeting is at 23:45."
    pattern = r'\b([01]\d|2[0-3]):[0-5]\d\b'  #0,1 or 2, (0,1,2,3) :0,1,2,3,4,5 (0to9)
    match = re.search(pattern, text)
    print(match.group() if match else "No match")
# time()

def postal():
    text = "My pin code is 560001."
    pattern = r'\b\d{6}\b' #0-9 6 times

    match = re.search(pattern, text)
    print(match.group() if match else "No match")
# postal()

def username():
    text = "farhan_pala"
    pattern = r'^[a-zA-Z0-9_]{3,15}$' # ^ : Start of string Ensures the match starts at the beginning of the string
                                      # {3,15}: Matches 3 to 15 characters from the previous set
                                      # $ End of string : Ensures the match goes till the end of the string

    match = re.match(pattern, text)
    print("Valid username" if match else "Invalid username")
# username()


def passw():
    text = "Farhan99"
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$' # .* : “match everything (except newlines) until something else stops it.”
                                                        # ?= : positive lookahead
                                                        # {8,} : ensures minimum 8
    """
    (?=.*[A-Za-z]) → ensures at least one letter exists anywhere
    (?=.*\d) → ensures at least one digit exists anywhere
    [A-Za-z\d]{8,} → ensures total length and allowed characters
    Together → all rules are enforced.
    
    Think of it like a password checklist:
    At least 1 letter ✅ (lookahead)
    At least 1 digit ✅ (lookahead)
    Minimum 8 chars ✅ (main match)
    Without lookaheads, rule 1 and 2 can’t be guaranteed.
    """


    match = re.match(pattern, text)
    print("Strong password" if match else "Weak password")
# passw()

def hashtags():
    text = "Loving the #VariableTribe #motivation"
    pattern = r'#\w+'   # \w: Word character, Matches letters (a-z, A-Z), digits (0-9), and underscore (_)
                        # +: One or more 

    matches = re.findall(pattern, text)  #re.findall returns all occurrences of the pattern in the string as a list.
    print(matches if matches else "No hashtags found")
# hashtags()

def quotedTxt():
    text = 'He said, "Knowledge is power" and left.'
    pattern = r'\".*?\"'

    matches = re.findall(pattern, text)
    print(matches if matches else "No quoted text found")
quotedTxt()