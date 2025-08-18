"""
This program checks the stackoverflow of elements in a list using class.

Overflow = trying to push when the stack is already full.
Underflow = trying to pop when the stack is already empty.
"""
class satckOverflow():
    def store(self):
        self.stack=[]
        self.limit=5

    def push(self,data):
        if len(self.stack) < self.limit: #[123, 123, 123, 123, 123 
            self.stack.append(data)
            return self.stack
        
        else:
            return "overflow"
        
stackOverflow=satckOverflow()
stackOverflow.store()

print(stackOverflow.push(123))
print(stackOverflow.push(345))
print(stackOverflow.push("abc"))
print(stackOverflow.push("rty"))
print(stackOverflow.push(987))
print(stackOverflow.push(999))
print(stackOverflow.push(102))
print(stackOverflow.push(999))