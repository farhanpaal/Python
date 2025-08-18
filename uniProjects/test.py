class satckOverflow():
    def abc(self):  # initialize values
        self.stack = []
        self.limit = 5

    def push(self, data):
        if len(self.stack) < self.limit:   # use self, not abc.self
            self.stack.append(data)
            return self.stack
        else:
            return "overflow"

stackOverflow = satckOverflow()
stackOverflow.abc()   # <-- must call abc() to initialize

print(stackOverflow.push(123))
print(stackOverflow.push(123))
print(stackOverflow.push(123))
print(stackOverflow.push(123))
print(stackOverflow.push(123))
print(stackOverflow.push(123))
