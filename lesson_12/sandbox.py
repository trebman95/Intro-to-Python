# Exercise 5. Inheritance. Spot and correct mistakes

# You should have the following hierarchy of classes:

 # Animal
 # │
 # ├── Mammal
 # │
 # ├── Bird
 # │
 # └── Fish

# Each class has the following attributes:

# - Animal name
# - Mammal name, age, number of legs
# - Bird name, age, can fly or not
# - Fish name, age, number of fins

# But, the provided code for these classes and their instances has several mistakes
# related to hierarchy, class attributes, and instance creation.

# Find and correct these mistakes to make the code work properly.
# Leave a comment in the code explaining what the problems were and why it wouldn't work.
# There are seven mistakes in the pre-code.

# Pre-code
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Mammal(Animal):
    def __init__(self, name, age, num_legs):
        super().__init__(name, age)
        self.num_legs = num_legs

class Bird(Animal):
    def __init__(self, name, age, can_fly):
        super().__init__(name, age)
        self.can_fly = can_fly

class Fish(Animal):
    def __init__(self, name, age, num_fins):
        super().__init__(name, age)
        self.num_fins = num_fins

tiger = Mammal('Tiger', 5, 4)
sparrow = Bird('Sparrow', 2, True)
goldfish = Fish('Goldfish', 2, 4)

print(tiger.__dict__)
print(sparrow.__dict__)
print(goldfish.__dict__)
