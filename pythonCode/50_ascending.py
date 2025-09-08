class Asc:
    def __init__(self,stack):
        self.stack=stack
    def sort(self):
        tmp=[]
        while len(self.stack)!=0:
            top=self.stack.pop()
            while len(tmp) !=0 and tmp[-1]>top:
                self.stack.append(tmp.pop())
            tmp.append(top)
        return tmp
asc=Asc([12,22,34])
print(asc.sort())