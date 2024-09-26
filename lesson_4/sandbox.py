# Exercise 9: Password Strength Checker
# Create a program that takes a password as input and checks its
# strength based on the following rules:

# If the password is less than 8 characters, print "Weak password."
# If the password is 8 to 12 characters long, print "Moderate password."
# If the password is more than 12 characters, print "Strong password

# You can use len() function to get the length of a given string.

password = input("Enter your password: ")

# <Your code here>

if len(password) < 8:
    print("Weak password.")
elif 8 <= len(password) <= 12:
    print("Moderate password")
elif len(password) >= 12:
    print("Strong password")