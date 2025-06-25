"""
WAP to check the longest string in a list
"""

def longest():
  longestStr=""
  lst=["pala","the","great"]
  for i in lst:
    if len(i)<len(longestStr):
      longestStr=i
  print(longestStr)
      

longest()