"""
This program checks the common elemets in two lists
"""

def Common():
  # list1=["pala",345,"the"]
  # list2=["paala",34,"name","the",345]


  # for i in list1:
  #   for j in list2:
  #     if i==j:
  #       print(f"{i} is common")

  a=[1,4,5,6]
  b=[4,6,7,4]
  c= list(set(a) & set(b))    #set removes duplicate elements
  print(c) 

    


Common()                       