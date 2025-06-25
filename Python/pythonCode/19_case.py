"""
WAP that takes in a string and prints weather it contains a lower case letter,
upper case letter or both
"""

# def CASE():
#     try:
#         name=input("Enter a string")
#     except ValueError as valerr:
#         print(valerr)
#     else:
#         upperLen=0
#         lowerLen=0
#         for i in name:
#             if i.islower():
#                 lowerLen+=1
#             elif i.isupper():
#                 upperLen+=1
       
#         if upperLen== len(name):
#             print("The whole string is in upper case")
#         elif lowerLen==len(name):
#             print("The whole string is in lower case")
#         elif upperLen > 0 and lowerLen > 0:
#             print("It contains both")
                        
# CASE()



# def CASE():
#     try:
#         name=input("Enter a string")
#     except ValueError as valerr:
#         print(valerr)
#     else:
#         capital=False
#         small=False
#         for i in name:
#             if i.islower():
#                 small= True
#             elif i.isupper():
#                 capital= True
       
#         if small == True and capital== True:
#             print("Both")
#         elif capital == True:
#             print("All capital")
#         else:
#             print("All small")

        
        
                        
# CASE()




# This last method takes two iteration, not good for memory management.

def check():
    a= input("Enter a string: ")
    # Using any() to check if string contains any uppercase or lowercase characters
    # Any returns True, if at least one item in iterable is true - It short-circuts, stops checking as soon as it finds a True.
    # It is parsed as whole generator expression, it is not executed like left to right
    capital=any(i.isupper() for i in a)
    small=any(i.islower() for i in a)

    if capital== True and small == True:
        print(" Contains both")
    else:
        if small == True:
            print("All small")
        else :
            print("All capital")

check()



