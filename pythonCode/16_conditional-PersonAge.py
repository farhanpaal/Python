""" 
QUESTION:
----------------------------
This program takes a person's age and checks if they are a child (0-12), teenager (13-19), young adult (20-39), middle-aged adult (40-59), or senior (60). Print an appropriate message for each group.

Algorithm:
------------------
1: Start
2: Define a function - ageCheck
3: try : age = take user input
3: except : print error message
4: else:
    if a < 0: print, invalid age
    elif a < 12: print the person is child
    elif a < 20: print the person is teenager
    elif a < 40: print the person is adult
    elif a < 60: print the person is of middle Age
    else : print senior
5: Call ageCheck function
6: END
"""

def ageCheck():
    try:a= int(input("Enter your Age: "))
    except: print("Error")
    else:
        if a<0: print("Invalid age")
        elif a<=12:
            print("Person is child")
        elif a<=20 :
            print("Person is teenager")
        elif a<=40 :
            print("Person Adult")
        elif a<=60 :
            print(" Middle Age")
        else:
            print("Senior")

ageCheck()


"""
Oops:
-------------------------
class Age:
    def __init__(self):
        try: a= int(input("Enter your Age: "))
        except: print("Error")
        else:
            if a<0: print("Invalid age")
            elif a<=12:
                print("Person is child")
            elif a<=20 :
                print("Person is teenager")
            elif a<=40 :
                print("Person Adult")
            elif a<=60 :
                print("Middle Middle Age")
            else:
                print("Senior")


Age()
"""