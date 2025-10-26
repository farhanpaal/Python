from abc import ABC, abstractmethod

# ABSTRACTION & ENCAPSULATION
class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.__employee_id = employee_id  # Encapsulated
        self.__salary = 0
    
    def get_employee_id(self):  # Controlled access
        return self.__employee_id
    
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Invalid salary")
    
    def get_salary(self):
        return self.__salary
    
    @abstractmethod
    def calculate_bonus(self):  # Abstraction
        pass
    
    def get_details(self):      # Polymorphism - common interface
        return f"ID: {self.__employee_id}, Name: {self.name}"

# INHERITANCE & POLYMORPHISM
class Manager(Employee):
    def __init__(self, name, employee_id, team_size):
        super().__init__(name, employee_id)
        self.team_size = team_size
    
    def calculate_bonus(self):  # Polymorphism - different implementation
        return self.get_salary() * 0.20
    
    def get_details(self):      # Polymorphism - overriding
        return f"{super().get_details()}, Team Size: {self.team_size}, Role: Manager"

class Developer(Employee):
    def __init__(self, name, employee_id, programming_language):
        super().__init__(name, employee_id)
        self.programming_language = programming_language
    
    def calculate_bonus(self):  # Polymorphism - different implementation
        return self.get_salary() * 0.15
    
    def get_details(self):      # Polymorphism - overriding
        return f"{super().get_details()}, Language: {self.programming_language}, Role: Developer"

# Usage
manager = Manager("Alice", "M001", 5)
developer = Developer("Bob", "D001", "Python")

manager.set_salary(80000)
developer.set_salary(60000)

employees = [manager, developer]

for emp in employees:
    print(emp.get_details())
    print(f"Bonus: ${emp.calculate_bonus()}")
    print("---")

# Output:
# ID: M001, Name: Alice, Team Size: 5, Role: Manager
# Bonus: $16000.0
# ---
# ID: D001, Name: Bob, Language: Python, Role: Developer
# Bonus: $9000.0
# ---