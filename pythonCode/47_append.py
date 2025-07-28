def myAppend():
    arr=[33,45,67,88,44]
    num= int(input("Enter number you want to append"))
    newArr= arr+[num] #append, we can also do prepend like this, just add num at start
    print(newArr)
myAppend()