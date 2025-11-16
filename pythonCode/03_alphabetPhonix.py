def Find(string):
    if string == "a": return "for apple"
    elif string == 'b': return "for ball"
    elif string == 'c': return "for cat"
    elif string == 'd': return "for dog"
    elif string == 'e': return "for elephant"
    elif string == 'f': return "for fish"
    elif string == 'g': return "for goat"
    elif string == 'h': return "for hat"
    elif string == 'i': return "for ice cream"
    elif string == 'j': return "for jug"
    elif string == 'k': return "for kite"
    elif string == 'l': return "for lion"
    elif string == 'm': return "for monkey"
    elif string == 'n': return "for nest"
    elif string == 'o': return "for orange"
    elif string == 'p': return "for parrot"
    elif string == 'q': return "for queen"
    elif string == 'r': return "for rabbit"
    elif string == 's': return "for 🐍snake"
    elif string == 't': return "for tiger"
    elif string == 'u': return "for umbrella"
    elif string == 'v': return "for van"
    elif string == 'w': return "for watch"
    elif string == 'x': return "for x-ray"
    elif string == 'y': return "for yak"
    elif string == 'z': return "for zebra"
    else: return "is not a valid character"


def Alphabet():
    a= input("Enter character: ").lower();
    store= Find(a)
    print(a,store)

Alphabet()
