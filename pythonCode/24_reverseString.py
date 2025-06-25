"""
This python program reverses a string
"""

def reverse():
  word=input("Enter a string: ")
  lengt= len(word)

  strin=''

  for i in range(lengt-1,-1,-1):
    strin+=word[i]
  print(strin)

reverse()