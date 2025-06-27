"""
This program takes a list of strings and returns a new list with only the strings that contain the letter input by user, also it prints even numbers which come in the range(5)
"""
def check():
    words = ["pala", "farhan", "elegant1"]
    char = input("Enter the character: ")
    result = [newWord for newWord in words if char in newWord]
  # [🔴 expression 🔴 for item in iterable if condition]
  #  expression defines what will be included in new list

    if not result:
        print("Not found")
    else:
        print(result)

check()

def Comprehension():
    magic=[lst for lst in range(5) if lst%2==0]
    print(magic)
Comprehension()