"""
Create an empty class called Car, then create two instances.
Add the following attributes for each of the instances: Make, Model, Year.
Create print statements to display the attributes of each one of the instances.
"""
class Car:
   pass

car1 = Car()
car2 = Car()

car1.make = "Toyota"
car1.model = "Corolla"
car1.year = "2012"

car2.make = "BMW"
car2.model = "i8"
car2.year = "2021"


print(f"Car 1: Make - {car1.make}, Model - {car1.model}, Year - {car1.year}")
print(f"Car 2: Make - {car2.make}, Model - {car2.model}, Year - {car2.year}")