"""
This program takes a list of strings and returns a new list with only the strings that contain the letter input by user
"""

def Search():
  newList=[]
  strings=["name","pala","sikha"]
  char = input("Enter a character you want to search")
  for string in strings:
    if char in string:
      newList.append(string)
  print(newList)
Search()