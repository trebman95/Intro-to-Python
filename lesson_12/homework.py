# Homework: Classes
# Read carefully until the end before you start solving the exercises.

# Practice the Basics

# Basic Class

class HouseForSale: # - Create an empty class HouseForSale
    pass

house1 = HouseForSale() # - Create an instances.
house1.number_of_rooms = 5 # - Add number_of_rooms and price as instance attributes.
house1.price = 400000

house2 = HouseForSale() # - Create an instance.
house2.number_of_rooms = 4 # - Add number_of_rooms and price as instance attributes.
house2.price = 270000

# - Create print statements that show the attribute values for the instances.
print(f"House 1: Number of rooms - {house1.number_of_rooms}, Price - {house1.price}")
print(f"House 2: Number of rooms - {house2.number_of_rooms}, Price - {house2.price}")

# ----------------------------------------------------------------------------------------------------------------------

# Instance Methods

# - Create a Computer class.


class Computer:
    def turned_on(self): # - Create an instance of the Computer class then call each method.
        print('Computer is turned on')

# - Create method:
#   - turn_on that prints Computer has Turned On
#   - turn_off that prints Computer has Turned Off
    def turned_off(self):
        print('Computer is turned off')

laptop = Computer()
laptop.turned_on()
laptop.turned_off()

# ----------------------------------------------------------------------------------------------------------------------

# Constructor with Parameters

# - Create a Dog class.
# - Dog should have a constructor with a name parameter.

class Dog:
    def __init__(self, name):
        self.name = name

# - Dog should have a method say_name that prints the name of the dog.
    def say_name(self):
        print(f'The name of the dog is {self.name}!')

identify = Dog('James')
identify.say_name()
# ----------------------------------------------------------------------------------------------------------------------

# Inheritance

# Create the classes that would make the following code possible, with the caveat that
# both Dog and Cat must inherit from Animal.

class Animal:
    def __init__(self, name = None):
        self.name = name

    def say_name(self):
        if self.name:
            print(self.name)
        else:
            print("I don't have a name")

    def speak(self):
        print(f"I can't speak!")

class Dog(Animal) :
    def speak(self):
        print(f"Woof!")

class Cat(Animal):
    def speak(self):
        print(f"Meow!")

animal = Animal()
animal.say_name()   # Prints: I don't have a name yet.
animal.speak()      # Prints: I can't speak!
#
dog = Dog('Fido')
dog.say_name()      # Prints: Fido
dog.speak()         # Prints: Woof!
#
cat = Cat('Max')
cat.say_name()      # Prints: Max
cat.speak()         # Prints: Meow!

# ----------------------------------------------------------------------------------------------------------------------

# Exercises
# Exercise 1: Books and Authors



# Create an empty class called Book. Then create three instances.
class Book:
    pass

# Add the following attributes for each of the instances: title, author, and publication_year.
book1 = Book()
book1.title = 'To Kill a Mockingbird'
book1.author = 'Harper Lee'
book1.pub_year = 1960

# Create print statements to display the attributes of each one of the instances.
print(f"Book 1: Title - {book1.title}, Author - {book1.author}, Publication Year - {book1.pub_year}")

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 2. Vehicle and Types of Vehicles

# Create a Vehicle class.
# - Its constructor should take the name and type of the vehicle and store them as instance attributes.
# - This Vehicle class should also have a show_type() instance method that prints out the
#   message: "<NAME_OF_VEHICLE> is a <TYPE_OF_VEHICLE>"

class Vehicle:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def show_type(self):
        print(f'{self.name} is a {self.type}')

# - Create Car and Bike classes that inherit from Vehicle.
# - Create instances of Car and Bike and make them show their types.

class Car(Vehicle):
    pass

class Bike (Vehicle):
    pass

my_car = Car('Toyota', 'Sedan')
my_bike = Bike('Mountain Bike', 'Off-Road')

my_car.show_type()
my_bike.show_type()

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 3. Spot and correct the mistakes

# - You are given a task to create a Car class.
# - Each car will have attributes for model and year.
# - Unfortunately, the given code below contains several mistakes.
# - Your task is to find and correct these mistakes to make the code run successfully.
# - Please include a comment in the code explaining the corrections you made and why.

# Pre-code
class Car:
 def __init__(self, model, year): #adding self in the constructor
    self.model = model #appending self to model
    self.year = year   #appending self to year
#
my_car = Car("Toyota", 2017) #Adding year parameter
print(my_car.model)
print(my_car.year)

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 4. SmartHome with Constructor

# Create a SmartHome class that has a constructor __init__ and a send_notification() method.
#
# The constructor should initialize the attributes:
# - home_name
# - location
# - number_of_devices
#
# send_notification() should print a notification including the home_name and location.

# Create instances for the following:
# Home Name      Location      Number of Devices
# Villa Rosa     New York      15 devices
# Green House    California    10 devices
# Sea View       Florida       20 devices

# Call the send_notification() method for each instance,
# passing a message reminding to turn off the lights.

class SmartHouse:
    def __init__(self, home_name, location, number_of_devices):
        self.home_name = home_name
        self.location= location
        self.number_of_devices = number_of_devices

    def send_notification(self, message):
        print(f'Notification for {self.home_name} at {self.location}: {message}')



smartHouse_Villa = SmartHouse('Villa Rosa', 'New York', '15')
smartHouse_Green = SmartHouse('Green House', 'California', '10')
smartHouse_Sea = SmartHouse('Sea View', 'Florida', '20')

smartHouse_Villa.send_notification('Remember to turn off the lights!')
smartHouse_Green.send_notification('Remember to turn off the lights!')
smartHouse_Sea.send_notification('Remember to turn off the lights!')

# ----------------------------------------------------------------------------------------------------------------------

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
        self.name = name # Corrected Mistake 1: should be self.name = name
        self.age = age  # Corrected Mistake 2: should be self.age = age

class Mammal(Animal):   # Corrected Mistake 3: "Animals" should be "Animal"
    def __init__(self, name, age, num_legs):
        super().__init__(name, age)
        self.num_legs = num_legs

class Bird(Animal): # Corrected the inheritance
    def __init__(self, name, age, can_fly):
        super().__init__(name, age)
        self.can_fly = can_fly

class Fish(Animal):   # Corrected Mistake 5: Fish inheriting from Animal now
    def __init__(self, name, age, num_fins):
        super().__init__(name, age)
        self.num_fins = num_fins # Ensure num_fins is an integer during object creation

tiger = Mammal('Tiger', 5, 4)
sparrow = Bird('Sparrow', 2, True) # Corrected Mistake 6: Passed the name and age
goldfish = Fish('Goldfish', 2, 4) # Corrected Mistake 7: Passed integer for num_fins

print(tiger.__dict__)
print(sparrow.__dict__)
print(goldfish.__dict__)
