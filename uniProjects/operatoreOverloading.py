# Operator overloading in Python is the ability to redefine or customize how built-in operators (like +, -, *, ==, etc.) work for user-defined classes by implementing special methods (like __add__, __sub__, __eq__, etc.).


# | Operator | Magic Method              |
# | -------- | ------------------------- |
# | +        | __add__(self, other)      |
# | -        | __sub__(self, other)      |
# | *        | __mul__(self, other)      |
# | /        | __truediv__(self, other)  |
# | //       | __floordiv__(self, other) |
# | %        | __mod__(self, other)      |
# | **       | __pow__(self, other)      |
# | <        | __lt__(self, other)       |
# | <=       | __le__(self, other)       |
# | ==       | __eq__(self, other)       |
# | !=       | __ne__(self, other)       |
# | >        | __gt__(self, other)       |
# | >=       | __ge__(self, other)       |
# | str()    | __str__(self)             |
# | repr()   | __repr__(self)            |

class Account:
    type='Account'
    count=0
    def __init__(self, name, branch, balance, category):
        self.name=name
        self.acno=Account.count+1
        self.branch=branch
        self.balance=balance
        self.category=category
        Account.count+=1

    def __lt__(self, other):
        return self.balance<other.balance
    def __add__(self,other):
        return self.balance+other.balance