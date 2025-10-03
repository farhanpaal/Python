class Customer:
    def __init__(self, name, mobile, address):
        self.__name=name
        self.mobile=mobile
        self.address=address

    #setter
    def setterFunc(self,newName):
        self.__name=newName
 
    # getter
    def getterFunc(self):
        print(self.__name)

    def __str__(self): #if we need string representation, python itself will call this.
        return f"Mr. {self.__name} is from {self.address}. Contact him on {self.mobile}"
    
 

cust= Customer("Pala",1234,"kashmir")
cust.setterFunc("Farhan ")
print(cust)
cust.getterFunc()