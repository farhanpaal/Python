# bank, "1000000", loan with intrest, credit, debit, deposit, accNo, 

class Customer:
    type="customer"
    count=0

    # getter
    @property
    def mobile(self):
        return self.__mobile

    @mobile.setter
    def mobile(self,value):
        if value<=0:
            raise ValueError("The value of mobile should not be less or equal to 0")
        else:
            self.__mobile=value

    def __init__(self, name,mobile, adr):
        self.__name=name
        self.mobile=mobile
        self.__adr=adr
        self.__id=Customer.count+1
        Customer.count+=1


class Account:
    type="account"
    count=0
    def __init__(self, cust, category, branch, balance, locker, debCard):
        self.cust=cust
        self.category=category
        self.branch=branch
        self.__balance=balance
        self.__locker=locker
        self.__debCard=debCard
    
    def shiftAcc(self,brnch):
        curBranch= str.split(self.branch, ':')
        tarBranch= str.split(brnch, ':')
        if tarBranch[0]==curBranch[0]:
            self.branch=brnch
        else:
            raise ValueError("invalid brance")
    def creditAm(self,amount):
        if amount>0 and amount<50000:
            self.__balance=amount
        else:
            raise ValueError("Invalid credit amount")
    def debAm(self, amount):
        if amount<10000 and amount>0:
            if(self.__balance - amount >100):
                self.__balance-=amount
                print("Amount debited successfully")
            else:
                raise ValueError("Invalid debit amount")

cust1= Customer("pala", 98009,"kulgam")
acc= Account(cust1, "saving", 'JK:SGR:2015', 2000,False, True)

acc.shiftAcc('JK:BML:2015')

print(acc.branch)
