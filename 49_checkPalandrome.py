"""
This program checks wheather string is a palandrome using stack.

eg: madam, perep, dad
"""

# class palandrome():
#     def __init__(self):
#         self.stack=[]
#     def check(self,data):
#         if (data==data[::-1]):
#             return f"{data} is a palindrome"
#         else:
#             return f"{data} is not a palindrome"


# palandrome= palandrome()

# print(palandrome.check("fellow"))


class palandrome():
    def __init__(self):
        self.stack=[]
        self.reservedData=""
    def check(self,data):
        for char in data:
            self.stack.append(char)
        while self.stack:
            self.reservedData = self.reservedData+self.stack.pop()
        
        return data==self.reservedData
        
palandrome= palandrome()
print(palandrome.check("dad"))