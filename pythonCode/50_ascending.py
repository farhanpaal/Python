class Asc:
    def __init__(self, stack):
        self.stack= stack #instance variable
    def sort(self):
        tmp=[]# it is local variable, not instance, because i dont' have to use it any where else
        return self.stack
    
asc= Asc([55,60,12,66,78]) #instance
print(asc.sort())