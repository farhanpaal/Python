"""
This program prints the factorial of a number which a user inputs.
 Here two methods are used to find the factorial:
 1) Procedural method
 2) Recursion
"""

# Method1
def factorial1():
  number= int(input("Print the number to find factorial of: "))
  a=number
  store=1
  b=0
  list=[]

  for i in range(a):
    list.append(a)
    a=a-1
  while b < len(list):
    store = store * list[b]
    b = b + 1
  print(f"The factorial of {number} is {store}")
  
factorial1()

#Method2: Recurssion
def factorial2():
  number= int(input("Print the number to find factorial of: "))
  def fact(n):
    if n == 0:
      return 1
    else:
      return n * fact(n-1)

  result = fact(number)
  print(f"The factorial of {number} is {result}")

factorial2()