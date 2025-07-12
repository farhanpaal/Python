def facto():
  try:
    a=int(input("Enter number"))
  except ValueError as valErr:
    print(valErr)
  else:
    fact=1
    for i in range(a):
      fact= fact*a
      a=a-1
    print(fact)
# facto()

def factoRecur():
  try:
    a=int(input("Enter number"))
  except ValueError as valErr:
    print(valErr)
  else:
    def fact(a):
      if a ==0 or a==1:
        return 1
      else:
        return fact(a-1) *a
    print(fact(a))

factoRecur()