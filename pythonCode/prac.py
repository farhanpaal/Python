"""

This program separates prime and composite numbers in two different lists from the one main list.
2 methods are used here.
"""

import sympy  
def prime():
    a = [23, 44, 7, 9, 11, 13, 15]
    for i in a:
        if sympy.isprime(i):
            print(i, "is prime")
        else:
            print(i, "is not prime")

# prime()

def prime2():
    list=[22,34,5,7,8,99,21,5]
    primeLst=[]
    compositeLst=[]
    for i in list:
        if i>1:
            for j in range(2, int(i**0.5) + 1):
                if i%j==0:
                    compositeLst.append(i)
                    break
            else:
                primeLst.append(i)
    
    print("prime numbers: ",primeLst)
    print("composite numbers: ",compositeLst)

            
 
prime2()

