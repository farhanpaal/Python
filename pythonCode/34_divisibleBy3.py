"""
This program takes a list of numbers and then separates from that the elements which are divisible by 3
"""

def divisibleBy3():
  print("\t---Enter 10 elements---")
  print("="*30)
  numbers=[]
  nums=[]
  for _ in range(10):
    try:
      num=int(input(f"Enter element {_+1}: "))
    except:
      raise Exception ("wrong input")
    else:
      nums.append(num)
  for i in nums:
    if i%3==0: numbers.append(i)
  print(f"Prime numbers from the list are {numbers}")
  
divisibleBy3()

