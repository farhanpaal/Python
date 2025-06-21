from libConvert import Main

class Lib(Main):
    def __init__(self):
        super().__init__()
        print(self.upperCase("farhan"))
        print(self.lowerCase("farhan"))
        print(self.sentenceCase("hello world my name iS fArhaN"))
Lib()