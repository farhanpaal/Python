class App:
    # type ="admin app"
    def __init__(self):
        self.name="farhan"
        self.__Passw="@123"
    def admin(self):
        return self.__Passw

app= App()
app1= App()
app.__Passw="23@"

app.type="admin2"
print(app.admin())
# print(app.type)

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
  