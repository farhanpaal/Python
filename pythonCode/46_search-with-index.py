"""
it will give index of element which user wants to find
It will give element of the index which user enters
"""

def search():
    arr=[3,44,56,7,9,55]
    num=int(input("enter data to searh: "))
    for i,val in enumerate(arr):
        if num == val:
            print("Element found at index", i)
            break
    else:
            print(" Data not found ")
          

    # num=int(input("enter index: "))
    # for i in range(len(arr)):
    #     if num == i:
    #         print(arr[i])

search()