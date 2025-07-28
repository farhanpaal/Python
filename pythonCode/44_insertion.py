# lst=[1,4,5,7,3]
# print(lst)
# lst.insert(1,100)
# print(lst)



#logically insert

Myarr=[33,44,55,22,11]
newArr=[]
index= int(input("Enter the index at which you want to input: "))
num=int(input("Enter the number you want to input"))

for i in range(len(Myarr)):
  if i==index:
    newArr.append(num)
  newArr.append(Myarr[i])

print(newArr)