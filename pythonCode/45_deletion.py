"""
This will deltete the element at the index which user will enter
"""

def deletion():
    arr=[1,33,45,67,8,88,97,56]
    newArr=[]
    index=int(input("Enter index to delete element you want."))
    for i in range(len(arr)):
        if i != index:
            newArr.append(arr[i])
    print(newArr)

deletion()

