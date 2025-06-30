"""
This is a basic program which finds mean, mode, median and some statistical analysis of elements which the user inputs .
"""

import statistics as stat
def avg():
  
  print("Basic instructions:")
  print("• Use -1 to exit from program.") 
  print("• Choose from multiple average calculation methods.")
  print("="*50)
  while True:
    print("• Choose one among the following:- ")
    print("1) Average Mean\n2) Mode\n3) Median\n4) Statistical Analysis\n5) exit")
    try:
      option= int(input())
      if option==-1 or option==5:
        print("Thanks for using our calculator")
        break
      elif option ==1:
        average()
      elif option ==2:
        mode()
      elif option ==3:
        median()
      elif option ==4:
        analysis()
      else:
        print("This choice doesn't exist, Choose right one\n")
    except ValueError as valerr :
      print(valerr,"\n")
def average():
  print("-------Calculating average-------")
  list=[]
  i=1
  while True:
    user_input=(input(f"Enter element no {i} -- [write \"done\" to finish]: "))
    try:
      if user_input.lower() == "done":
        break
      store= int(user_input)
      list.append(store)
      i+=1
    except ValueError as valerr:
      print(valerr)
  average= stat.mean(list)
  print(f"•• The values you enetered are as: {list}")
  print(f"•• Average of your values is: {average}")
  print("-"*50,"\n")

def mode():
  print("-------Calculating Mode-------")
  list=[]
  i=1
  while True:
    user_input=(input(f"Enter element no {i} -- [write \"done\" to finish]: "))
    try:
      if user_input.lower() == "done":
        break
      store= int(user_input)
      list.append(store)
      i+=1
    except ValueError as valerr:
      print(valerr)
  mode= stat.mode(list)
  print(f"•• The values you enetered are as: {list}")
  print(f"•• Mode of your values is: {mode}")
  print("-"*50,"\n")

def median():
  print("-------Calculating Median-------")
  list=[]
  i=1
  while True:
    user_input=(input(f"Enter element no {i} -- [write \"done\" to finish]: "))
    try:
      if user_input.lower() == "done":
        break
      store= int(user_input)
      list.append(store)
      i+=1
    except ValueError as valerr:
      print(valerr)
  median= stat.median(list)
  print(f"•• The values you enetered are as: {list}")
  print(f"•• median of your values is: {median}")
  print("-"*50,"\n")

def analysis():
  print("-------Doing statistical Analysis-------")
  list=[]
  i=1
  while True:
    user_input=(input(f"Enter element no {i} -- [write \"done\" to finish]: "))
    try:
      if user_input.lower() == "done":
        break
      store= int(user_input)
      list.append(store)
      i+=1
    except ValueError as valerr:
      print(valerr)
  mean= stat.mean(list)
  mode= stat.mode(list)
  median= stat.median(list)
  total= len(list)
  sumAll= sum(list)
  maxi=max(list)
  least=min(list)
  
  print(f"Mean: {mean}")
  print(f"Mode: {mode}")
  print(f"Median: {median}")
  print(f"Total elements: {total}")
  print(f"Sum of elements: {sumAll}")
  print(f"Max: {maxi}")
  print(f"Min: {least}")
  print("-"*50,"\n")

avg()