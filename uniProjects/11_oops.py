class Customer:
    type='customer'
    count=0


    @property
    def mobile(self):
        return self.__mobile

    @mobile.setter
    def mobile(self,value):
        if(value<=0):
            raise ValueError("the value should be greater or equal to 0")
        else:
            self.__mobile=value

    
    def __init__(self, name, mbn, addr):
        self.__name=name
        self.__mbn=mbn
        self.__addr=addr
        self.__id= Customer.count
        Customer.count+=1
    
    def setterFunc(self, data):
        self.__name=data

    def getterFunc(self):
        return [self.__name, self.__mbn, self.__addr]

    def __str__(self):
        return f"Name: Mr. {self.__name}, Mobile: {self.__mbn}, Address: {self.__addr}, Id: {self.__id}"
    
   


c1= Customer("pala",6767,"kmr")
c2= Customer("paal",7676,"mkr")

# print(" ".join(c2.store))
# print(c1)
c1.setterFunc("tata")
print(c1.getterFunc())