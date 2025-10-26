# abstraction means diding complex implementation details and showing only essential features.

from abc import ABC, abstractmethod
# from abc import ABC, abstractmethod is used to create abstract classes and abstract methods in Python.

# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
    def honk(self):  # Concrete method
        return "Beep beep!"

# Concrete classes implementing abstract methods
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started with key"
    
    def stop_engine(self):
        return "Car engine stopped"

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started with button"
    
    def stop_engine(self):
        return "Motorcycle engine stopped"

class ElectricCar(Vehicle):
    def start_engine(self):
        return "Electric motor activated silently"
    
    def stop_engine(self):
        return "Electric motor deactivated"

# Usage
vehicles = [Car(), Motorcycle(), ElectricCar()]

for vehicle in vehicles:
    print(vehicle.start_engine())
    print(vehicle.honk())  # Inherited concrete method
    print(vehicle.stop_engine())
    print("---")

# Cannot instantiate abstract class
# v = Vehicle()  # ❌ Error - abstract class