# class Main:
#     naam=""
#     kaam=""
#     def __init__(self):
#         self.name="pala"
#         self.password="@123"
#         self.sem=1
 


# admin=Main()
# print(admin.name)
# print(admin.password)
# print(admin.sem)
  


class Admin:

    #getter
    def adminName(self):
       return self.__name
    
    #setter
    def setterFunc(self, setter):
        self.__name=setter

    def __init__(self):
        self.__name="pala"
        self.__password="@123"
        self. __sem=1
admin=Admin()
admin.setterFunc('dsfsd')  
print(admin.adminName())



# class Main:
#     def __init__(self):
#         self.name="pala"
#         self.__password="@123"
#         self.sem=1
    
#     def read(self):
#         return self.__password
 
# admin=Main()
# print(admin.name)
# print(admin.read())
# print(admin.sem)
  

