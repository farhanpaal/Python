# This program is demonstrating inheritance 

class School1:
    def abouts1(self):
        print("This is school1")
class School2(School1):
    def abouts2(self):
        print("This is school2")

s2=School2()

s2.abouts2()
s2.abouts1()