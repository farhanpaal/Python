import math

a= float(input("Enter coefficient a: "))
b= float(input("Enter coefficient b: "))
c= float(input("Enter coefficient c: "))

discr= b* b - 4*a*c

if discr>0:
  print("Two real  and distinct roots are: ")
  root1=(-b+math.sqrt(discr))/(2*a)
  root2=(-b-math.sqrt(discr))/(2*a)
  print(f"root1: {root1}, root2: {root2}")
elif discr== 0:
  root = -b / (2*a)
  print("One real and repeated root:")
  print("Root =", root)
elif discr<0: 
  realPart = -b / (2*a)
  imagPart = math.sqrt(-discr) / (2*a)
  print("Two complex roots:")
  print("Root 1 = {} + {}i".format(realPart, imagPart))
  print("Root 2 = {} - {}i".format(realPart, imagPart))

