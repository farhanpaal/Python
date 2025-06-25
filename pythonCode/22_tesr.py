"""
WAP that checks weather a number is prime or not
"""

from math import sqrt
def prime():
  num = int(input("Enter number"))
  sqr= int(sqrt(num))
  prim= False
  compos= False
  for i in range(2,sqr):
    if num%i!=0:
      prim=True
      break
    else:
      compos=True
      break
  if prim==True:
    print("It is prime")
  else:
    print("Not prime")

prime()