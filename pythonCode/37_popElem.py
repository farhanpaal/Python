"""
This program removes the element from the list whic user inputs using while loop
"""

def remove():
  lst = [1, 5, 6, 6, 9, 6, 3, 2, 12]
  user= int(input("enter number you want to remove from list: "))
  index = 0
  while index < len(lst):
    num = lst[index]
    if user == num:
      lst.pop(index)
    else:
      index += 1
  
  print(lst)
remove()