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
  


# class Admin:
#     def __init__(self):
#         self.__name="pala"
#         self.__password="@123"
#         self. __sem=1
#     def adminName(self):
#        return self.name
# admin=Admin()
# admin.__name= 'dsfsd'
# print(admin.adminName())



class Main:
    def __init__(self):
        self.name="pala"
        self.__password="@123"
        self.sem=1
    
    def read(self):
        return self.__password
 
admin=Main()
print(admin.name)
print(admin.read())
print(admin.sem)
  

