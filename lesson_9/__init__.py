# Even/Odd Checker Function
# Your task is to write a function that determines if a given integer is even or odd. The function should
# print Even for even numbers and Odd for odd numbers.

# What You Need to Check
# - Determine whether the input number is even or odd.
# - An even number can be exactly divided by 2 without a remainder.
# - An odd number leaves a remainder of 1 when divided by 2.

# Define a function is_even_odd(number) here

def is_even_odd(number):
    if number % 2 == 0:
        print('Even')
    else:
        print('Odd')

# Test the function calling it using a variety of numbers like: 1, 10, 5.5, 9

is_even_odd(1)
is_even_odd(10)
is_even_odd(5.5)
is_even_odd(9)
