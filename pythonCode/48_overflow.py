"""
This program checks the stackoverflow of elements in a list using class.
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
print(stackOverflow.push(123))
print(stackOverflow.push(123))
print(stackOverflow.push(123))
print(stackOverflow.push(123))
print(stackOverflow.push(123))
print(stackOverflow.push(123))
print(stackOverflow.push(123))
print(stackOverflow.push(123))
print(stackOverflow.push(123))
print(stackOverflow.push(123))

