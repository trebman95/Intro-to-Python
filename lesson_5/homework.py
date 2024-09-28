# Homework Lesson 5 - Workshop - Homework

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

# Challenge 1
# Make a number Positive
#
# Create a variable called my_number and set it to any integer value.
# Write code to make the number positive if it's negative, and keep it
# as is if it's already positive or zero.
#
# Example:
# Input: -3 => Output: 3
# Input: 5 => Output: 5

my_number = int(input("Enter an integer value: "))

if my_number < 0:
    my_number = abs(my_number)
    print(my_number)
else:
    print(my_number)


# ---------------------------------------------------------------------

# Challenge 2
# BinGo!
#
# If the number is divisible of 3, print “Bin”
# If the number is divisible of 7, print “Go”
# For numbers which are divisible of 3 and 7, print “BinGo”
# Otherwise, print the original number: “{number} is just a number”

bingo_num = int(input('Enter a number: '))

if bingo_num % 3 == 0 and bingo_num % 7 == 0:
    print("BinGo")
elif bingo_num % 3 == 0:
    print("Bin")
elif bingo_num % 7 == 0:
    print("Go")
else:
    print(f"{bingo_num} is just a number")


# ---------------------------------------------------------------------

# Challenge 3
# Find the middle number
#
# Given three different numbers x, y, and z, find the number that is neither
# the smallest nor the largest and print it.
#
# Example:
# x = 1, y = 5, z = 3 => Output: 3

x = int(input('Enter x value: '))
y = int(input('Enter y value: '))
z = int(input('Enter z value: '))

if (x > y) and (x < z) or (x < y) and (x > z):
    middle_num = x
elif (y > x) and (y < z) or (y < x) and (y > z):
    middle_num = y
else:
    middle_num = z

print(f'{middle_num} is the middle number')


# ---------------------------------------------------------------------

# Challenge 4
# Palindrome Numbers
#
# Ask a user to input a number.
# Write a program to check if the given number is a palindrome.
# It should print True if the number is a palindrome and False if it is not.
#
# Palindrome number: 121, 898

num = input('Enter a number: ')

if num == num[::-1]:
    print("True")
else:
    print("False")


# ---------------------------------------------------------------------

# Challenge 5
# Reverse a string
#
# You're part of a team working on analyzing customer reviews for a new video game.
# Due to a software glitch, some reviews have been recorded in reverse with punctuation
# at the beginning instead of the end. Your task is to correct these reviews so that they
# are in the correct order and the punctuation is appropriately placed at the end of the
# sentence or word.
#
# Example: "tcefreP!" -> Perfect!

glitch_str = input("Enter you glitch word: ")
reversed_str = glitch_str[::-1]
corrected_str = ""

if reversed_str and reversed_str[0] in "!.,":
    corrected_str = reversed_str[1:] + reversed_str[0]
else:
    corrected_str = reversed_str


print(corrected_str)



