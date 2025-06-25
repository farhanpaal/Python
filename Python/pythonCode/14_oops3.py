# class Fun1:
#     def __init__(self):
#         print("hello world")

# class Fun2(Fun1):
#     pass
#     # def __init__(self):
#         # print("hello Farhan Pala")
    
# Fun2()




# add= lambda x,y,z: x+y+z
# print(add(3,5,9)) 




# class Main:
#     def __init__(self):
#         self.add= lambda a,b: a+b

# main=Main()
# print(main.add(2,4))



class Credentials:
    def __init__(self):
        self.__password=12345
    
    #getter / accessor
    def getPassword(self):
        print(self.__password)

    #setter / mutator
    def setPassword(self,passw):
        self.__password = passw
    
credentials=Credentials()
credentials.setPassword("pala")

credentials.getPassword()