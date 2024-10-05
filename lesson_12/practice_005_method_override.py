"""
Take the Dog and Cat classes you built in the last practice and
override the greeting method to give the following output:

Dog: "Hello <NAME>, my name is <DOG_NAME> and I'm a dog! 🐶"
Cat: "Hello <NAME>, my name is <CAT_NAME> the cat and I hate you. 😾"
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def greeting(self, name):
        print(f'Hello {name}, I am {self.name}')

class Dog(Animal):
    def greeting(self, name):
        print(f'Hello {name}, my name is {self.name} and I am a dog!')

class Cat(Animal):
    def greeting(self, name):
        print(f'Hello {name}, my name is  {self.name} the cat and I hate you!')

dog = Dog('Fido')
dog.greeting('Joseph')