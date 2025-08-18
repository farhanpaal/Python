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
    def pop(self):
        if self.stack == []:
            print("stack underflow")
        else:
            self.stack.pop()
    
stackUnderflow=stackUnderflow()

print(stackUnderflow.push(1232))
print(stackUnderflow.push(345))
print(stackUnderflow.push(424))
stackUnderflow.pop()
stackUnderflow.pop()
stackUnderflow.pop()
stackUnderflow.pop()
 