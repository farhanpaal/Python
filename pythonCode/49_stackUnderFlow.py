"""
This program checks stack underflow

Overflow = trying to push when the stack is already full.
Underflow = trying to pop when the stack is already empty.
"""
class stackUnderflow():
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
        return self.stack
    def remv(self):
        if self.stack==[]:
            print("stack underflow")
        else:
            self.stack.pop()
        
stackUnderflow=stackUnderflow()
print(stackUnderflow.push(123))
print(stackUnderflow.push(456))
print(stackUnderflow.push(789))
print(stackUnderflow.push("abc"))
print(stackUnderflow.push("def"))

stackUnderflow.remv()
stackUnderflow.remv()
stackUnderflow.remv()
stackUnderflow.remv()
stackUnderflow.remv()
stackUnderflow.remv()