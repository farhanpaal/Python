"""
This program checks weather a number is prime or not
"""

from math import sqrt
def prime():
  num = int(input("Enter number: "))

  if num <= 1:
    print("Not prime")
    return

  if num == 2:
    print("It is prime")
    return

  sqr = int(sqrt(num))
  is_prime = True

  for i in range(2, sqr + 1):
    if num % i == 0:
      is_prime = False
      break

  if is_prime:
    print("It is prime")
  else:
    print("Not prime")

prime()