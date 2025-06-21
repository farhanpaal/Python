def firstAlphabet(string):
    print("The first alphabet of",string,"is",string[0],sep=" ")
def lastAlphabet(string):
    length= len(string)
    print("The last alphabet of",string,"is",string[length-1],sep=" ")
def indexCustom(string):
    a= int(input("Enter character Index: "))
    
    print("The index of",string,"at",a,"at",string[a])


def charFinder():
    print("Character Finder")
    print("--------------")
    b=input("Enter the string:\n ")
    print("Options:\n 1) Find first alphabet.\n 2) Find last alphabet\n 3) Find custom index character")
    option=int(input(" "))

    if option == 1: return firstAlphabet(b)
    if option == 2: return lastAlphabet(b)
    if option == 3: return indexCustom(b)

charFinder()
