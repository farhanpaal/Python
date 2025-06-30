def main():
  a,n=0,1
  siList =[] 
  ciList =[] 
  list=[]
  i=1
  
  # total=int(input("Enter total number of users: "))
  print("BASIC INSTRUCTIONS: \n To end the program enter -1. \n")
  while True:
    try:
        total = int(input("Enter total number of users: "))
        if total == -1:
          break
        if total < -1:
            raise ValueError("Number of users must be positive.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}")
  
  while len(list)<total:
    try:
      principal= int(input(f"Enter principle amount of user {i}: "))
      if principal == -1:
        break
      rate= int(input(f"Enter rate of user {i}: "))
      if rate == -1:
        break
      time=int(input(f"Enter time of user {i}: "))
      if time == -1:
        break
      user_data=[principal, rate, time]
      list.append(user_data)
      i=i+1
    except ValueError as valerr:
      print(valerr)
      
  while a<len(list):
    si = (list[a][0]*list[a][1]*list[a][2])/100
    principal=list[a][0]
    r=list[a][1]
    t=list[a][2]
    amount = principal * pow((1 + r/(100*n)), n*t)
    ci=amount-principal
    
    siList.append(si)
    ciList.append(ci)
    a=a+1
  print("==========================")
  print(f"SI of first {a} users are {siList}")
  print(f"CI of first {a} users are {ciList}")
main()

