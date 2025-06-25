"""
This program checks the longest string in a list
"""

def longest():
  longestStr=""
  lst=["pala","the","great","FarhanPala"]
  for i in lst:
    if len(i)>len(longestStr):
      longestStr=i
  print(longestStr)
      

longest()