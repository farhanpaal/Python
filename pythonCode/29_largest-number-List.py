"""
This program finds largest number in a list and prints that
"""

def find():
  numbers=[66,99,668,9,88]
  # print(max(numbers))
  store=0
  for i in numbers:
    if i>store:
      store=i
  print(store)

find()