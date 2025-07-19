"""
This program prints the frequency of elements in a list
"""
def freq():
  lst=[3,4,6,2,1,3,4,2,3,6,3,2]
  lstSet=list(set(lst))
  i=0
  while i<len(lstSet):
    print(f"{lstSet[i]} is printed {lst.count(lstSet[i])} times.")
    i+=1
freq()