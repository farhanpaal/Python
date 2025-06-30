def avg():
  while True:
    print("Basic instructions:")
    print("• Use -1 to exit from program.") 
    print("• Choose from multiple average calculation methods.")
    print("="*50)
    print("1) Average Mean\n2) Mode\n3) Median\n4) Statistical Analysis\n5) exit")
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
def average():
  print("-------Calculating average-------\n")
  list=[]
  i=1
  while True:
    user_input = input(f"Enter element no {i} -- [write \"done\" to close]: ")
    if user_input.lower() == "done":
      break
    try:
      store = int(user_input)
      list.append(store)
      i+=1
    except ValueError:
      print("Invalid input! Please enter a number or 'done'.")
  
  if list:
    avg = sum(list) / len(list)
    print(f"Numbers: {list}")
    print(f"Average: {avg:.2f}")
  else:
    print("No numbers entered!")

  
  

avg()