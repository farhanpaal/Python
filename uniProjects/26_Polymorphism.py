# Polymorphism means same interface for different data types, ability to use the same method name for different types.
# Polymorphism = "One interface, multiple implementations"

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def make_sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    def make_sound(self):
        return "Meow!"

# NOW we can create objects and use the function
def animal_sounds(animals):
    for animal in animals:
        print(f"{animal.name} says: {animal.make_sound()}")

# object bundling the data
animals = [
    Dog("Rex", "German Shepherd"),
    Cat("Mittens", "Black"),
    Dog("Max", "Labrador")
]

animal_sounds(animals)