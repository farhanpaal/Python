"""
A module libconvert is used here to convert the string in different cases
------------------------------------

That library:libConvert.py

class Main:
  def __init__(self):
      self.upperCase= lambda string: string.upper()
      self.lowerCase= lambda string: string.lower()
      self.sentenceCase= lambda string: string.title()

"""


from libConvert import Main

class Lib(Main): 
    def __init__(self):
        super().__init__()
        print(self.upperCase("farhan"))
        print(self.lowerCase("farhan"))
        print(self.sentenceCase("hello world my name iS fArhaN"))
Lib()