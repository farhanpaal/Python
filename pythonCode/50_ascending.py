class Asc():
    def __init__(self,stack):
        self.stack=stack
    def sort(self):
        tmp=[]
        while len(self.stack)!=0:
            top=self.stack.pop()
            while len(tmp)!=0 and top<tmp[-1]:
                self.stack.append(tmp.pop())
            tmp.append(top)
        return tmp


asc=Asc([34,66,76,3,23])
print(asc.sort())


