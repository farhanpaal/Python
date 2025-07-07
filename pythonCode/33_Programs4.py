"""
This program takes odd numbers from a list and stores them in other list and then prints 
"""

def oddNum():
  lst=[1,2,3,4,5,6,7,8,99,65,78,5]
  oddList=[]
  for i in lst:
    if i%2!=0:
      oddList.append(i)

  print(oddList)
# oddNum()



"""
this program prints the total number of words in a string
"""
def wordCount():
  string="farhan is my name"
  elem= string.split()
  print(len(elem))
# wordCount()




"""
This program filters out the element which starts with any specific alphabet
"""
def startWith():
  string=["pala","and","shahid","ahsaan","rubait"]
  store=[]
  for i in string:
    if i.lower().startswith("a"):
      store.append(i)
  print(store)

# startWith()




"""
This program prints out if the year user enters is leap or not
"""
def leap():
  try:
    year = int(input("Enter the year"))
  except:
    raise Exception("Wrong input")
  else:
    if year / 4 == 0:
      print(f"{year} is a leap year")
    else:
      print(f"{year} is not a leap year")

leap()
