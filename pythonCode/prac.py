"""
This program takes a list of numbers and then separates from that the elements which are divisible by 3
"""

nums=[33,45,4,6,7,99,9,5]
mul=[]
for i in nums:
  if i%3==0: mul.append(i)
print(mul)