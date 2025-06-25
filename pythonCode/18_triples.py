""""
This program takes 3 numbers
Checks if they are pythagoras triples. If they do ,
Print "These numbers from pythagoras triple." If they don't,
Print These numbers are not from pythagoras triple".
"""
# 3 4 5 are pythagoras triple

def triples():
        try:
            firstNo= int(input("Enter first number: "))
            secondNo= int(input("Enter second number: "))
            thirdNo= int(input("Enter third number: "))
        except ValueError as valerr:
            print(valerr)
        else:
            if firstNo**2 + secondNo**2 == thirdNo**2:
                print("It is a pythagoras triplet")
            else:
                print("It is not a pythagoras triple")



triples()