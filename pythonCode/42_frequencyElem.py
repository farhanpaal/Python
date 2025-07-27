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
# freq()



def freq2():
  lst=[3,4,6,2,1,3,4,2,3,6,3,2]
  dictLst={}


  print(dictLst)
  index=0
  while index< len(lst):
    if lst[index] in dictLst: 
      dictLst[index]=dictLst[index]+1
    else:
      dictLst[index]=1
    index+=1

  print(dictLst)

freq2()