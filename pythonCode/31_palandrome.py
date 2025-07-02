"""
This program takes a string and returns True if the string is palandrome otherwise false.

eg of palandrome: level, madam, 12321
"""


"""---------Methiod 1---------"""
def palandrome():
  userInput=input("Enter a string: ") #asbbsa
  strLength= len(userInput)
  flag=True
  for i in range(strLength // 2):
    if userInput[i] != userInput[strLength - 1 -i]: #a != a
      flag=False
      break
  if flag:
    print("Palandrome")
  else:
    print("Not a palandrome")
# palandrome()


"""---------Methiod 2---------"""
def palandrome2():
  userInput=input("Enter a string: ") #asbbsa
  strLength= len(userInput)
  count =0
  lg=strLength-1
  for i in range(lg):
    if userInput[i] == userInput[lg]:
      count=count+1
      lg=lg-1
  lg=len(userInput)
  if count == lg-1:
    print("This is a palandrome")
  else:
    print("Not a palandrome")
# palandrome2()


"""---------Methiod 3---------"""
def palandrome3():
  name=input("Enter a string: ")
  revName=name[::-1]
  if name==revName:
    print("This is palandrome")
  else:
    print("This is not a palandrome")
palandrome3()