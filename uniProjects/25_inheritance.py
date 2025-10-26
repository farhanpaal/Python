# Inheritance means creating new classes (child classes) from existing ones (parent classes), inheriting attributes and methods.

class Parent:
    def __init__(self, name, age):
        self.name = name    
        self.age = age      
    
    def display(self):
        return f"Parent: {self.name}, {self.age} years old"

class Child(Parent):
    def __init__(self, name, age, school):
        super().__init__(name, age)  # Initialize Parent part
        self.school = school          # Initialize Child part
    
    def display(self):
        return f"Child: {self.name}, {self.age} years old, goes to {self.school}"

child_obj = Child("Mamoon", 15, "High School")
parent_obj = Parent("Ahmad", 40)   

print(child_obj.display())    
print(parent_obj.display())   
print(child_obj.age)          
print(parent_obj.age)        