#⭕ Q1: Car class – attributes: brand, model, year; method: display details.
# class Car:
#     def __init__(self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year
#     def display(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

# car= Car("Tayota",22,2022)
# car.display()


#⭕ Rectangle class – attributes: length, width; methods: area(), perimeter().
# class Reactangle:
#     def __init__(self, length, width):
#         self.length=length
#         self.width=width
#     def area(self):
#         print(self.length*self.width)

#     def perimeter(self):
#         return 2*(self.length*self.width)

# reactangle= Reactangle(23,4)

# reactangle.area()
# print(reactangle.perimeter())
        

#⭕ BankAccount class – attributes: owner, balance; methods: deposit(), withdraw().

class BankAccount:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance

    def deposit(self, amount):
        self.balance +=amount
        return self.balance

        
    def withdraw(self, amount):
        self.balance -=amount

        return self.balance
        
bankAcc= BankAccount("Mr. Anatuliya",2000)
print(bankAcc.deposit(200))
print(bankAcc.withdraw(100))
