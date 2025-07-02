"""
This program finds the second largest element in an array
"""

def secondLar():
  list = [23, 55, 76, 3]
  maxNum = max(list)
  
  secondLar = 0
  for i in list:
    if i>secondLar and i<maxNum:
      secondLar=i
  print(secondLar)
secondLar()