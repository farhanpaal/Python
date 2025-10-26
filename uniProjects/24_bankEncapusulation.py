# Encapsulation means bundling data and methods that operate on that data within a single unit (class), and restricting direct access to some components.

class Bank:
    def __init__(self, name, balance):
        self.name=name
        self.__balance=balance

    def initialBal(self):
        return self.__balance
    
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Deposited ${amount}")
        else:
            print("Invalid amount")
    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount
            print(f"withdrew ${amount}")
        else:
            print("Insufficient funds")
 
    def get_balance(self):
        return self.__balance

bank= Bank("farhan",234)
print(f"Initial Bank Balance: ${bank.initialBal()}")

bank.deposit(500)
bank.withdraw(500)
print(f"total left: ${bank.get_balance()}")
