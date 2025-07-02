"""
This program takes a string and returns number of vowels in the string.
"""

# def vowel():
#   string= input("Enter string: ")
#   store=0
#   for i in string:
#     if i == 'a' or i =='A':
#       store+=1
#     elif i  == 'e' or i=='E':
#       store+=1
#     elif i  == 'i' or i=='I':
#       store+=1
#     elif i  == 'o' or i=='O':
#       store+=1
#     elif i  == 'u' or i=='U':
#       store+=1
#   print(store)
    
# vowel()

def vowelCount():
  a=input("Enter your string: ")
  vowel="aeiou"
  vowelCount=0
  voweltore=""
  for i in a:
    if i.lower() in vowel:
      vowelCount+=1
      voweltore+=(i+", ")

  print(f"There are {vowelCount} vowels and they are {voweltore}")
vowelCount()