"""
This program checks stacoverflow. Means is there more than limit in stac
"""

class stackOverflow():
    def __init__(self):
        self.stack=[]
        self.limit=5
    def push(self,data):
        self.stack.append(data)
        print(self.stack)

stackOverflow= stackOverflow()
stackOverflow.push(1234)


