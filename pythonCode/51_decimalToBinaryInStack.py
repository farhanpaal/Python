#WAP to convert decimal to binary


#method1
def dTb(n):
    decimalNum=[]
    if n==0:
        return 0
    
    while n>0:
        decimalNum= str(n%2) + decimalNum
        n=n//2
    return decimalNum
  

# print(dTb(45))


#method2
print(bin(45)[2:])