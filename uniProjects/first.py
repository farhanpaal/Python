def main():
  a,n=0,1
  siList =[] 
  ciList =[] 
  list=[]
  print(len(list))
  i=1
  total=int(input("Enter total number of users: "))
  while len(list)<total:
    principal= int(input(f"Enter principle amount of user {i}: "))
    rate= int(input(f"Enter rate of user {i}: "))
    time=int(input(f"Enter time of user {i}: "))
    user_data=[principal, rate, time]
    list.append(user_data)
    i=i+1

  while a<len(list):
    si = (list[a][0]*list[a][1]*list[a][2])/100
    principal=list[a][0]
    rate_percent=list[a][1]
    t=list[a][2]
    
    # Convert rate from percentage to decimal
    r = rate_percent / 100
    
    # Correct compound interest formula: A = P(1 + r/n)^(nt)
    amount = principal * pow((1 + r/n), n*t)
    ci = amount - principal
    
    siList.append(si)
    ciList.append(ci)
    a=a+1
  print(siList)
  print(ciList)
main()

