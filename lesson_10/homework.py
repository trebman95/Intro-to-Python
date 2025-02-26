# Homework Lesson 10 - Workshop - Homework

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

################################################################################
### When solving coding challenges, think about the time complexity (Big O). ###
################################################################################

# Challenge 1
# Multiplication of a three-digit number
#
# A program gets a three-digit number and has to multiply all its digits.
# For example, if a number is 349, the code has to print the number 108, because 3*4*9 = 108.
#
# Hints:
# Use the modulus operator % to get the last digit.
# Use floor division to remove the last digit

def multiplication_of_three(number):
    result = 1
    for i in range(3):
        result = result * (number % 10)
        number = number // 10

    print(f'result: {result}')

multiplication_of_three(349)

#def multiplication_of_three(number):
#    mult = 1

#    while number > 0:
#        digit = number % 10
#        mult *= digit
#        number //= 10
#    return mult

#print(multiplication_of_three(349))

#def multiplication_of_three(number):
# Your code here
#   mult = 1

#   for i in str(number):
#    mult *= int(i)

#   return mult

#print(multiplication_of_three(349))

# ---------------------------------------------------------------------

# Challenge 2
# Sum and multiplication of even and odd numbers.
#
# You are given an array of integers. Your task is to calculate two values: the sum of
# all even numbers and the product of all odd numbers in the array. Please return these
# two values as a list [sum_even, multiplication_odd].
#
# Example
# For the array [1, 2, 3, 4]:
#
# The sum of all even numbers is 2 + 4 = 6.
# The product of all odd numbers is 1 * 3 = 3.
# The function should return the list [6, 3].

def sum_even_and_product_odd(arr):
    # Initialize variables for the sum of even numbers and the product of odd numbers
    # Your code here
    sum_even = 0
    product_odd = 1
    for num in arr:
        if num % 2 == 0:
            sum_even += num
        else:
            product_odd *= num
    return [sum_even, product_odd]

print(sum_even_and_product_odd([1, 2, 3, 4]))


# ---------------------------------------------------------------------

# Challenge 3
# Invert a list of numbers
#
# Given a list of numbers, return the inverse of each. Each positive becomes a negative,
# and the negatives become positives.
#
# Example:
# Input: [1, 5, -2, 4]
# Output: [-1, -5, 2, -4]


def invert_list(arr):
    for i in range(len(arr)):
        arr[i] = -arr[i]
        return arr


print(invert_list([1, 5, -2, 4]))


# ---------------------------------------------------------------------

# Challenge 4
# Difference between
#
# Implement a function that returns the difference between the largest and the
# smallest value in a given list.
# The list contains positive and negative numbers. All elements are unique.
#
# Example:
# Input: [3, 5, 7, 2]
# Output: 7 - 2 = 5

def max_diff(arr):
    # Check if the list is empty
    # If it is, return 0 as there's no difference to be calculated
    if len(arr) == 0:
        return 0

    return max(arr) - min(arr)

# If the list is not empty,
# proceed with the rest of the code.

# Your code here

print(max_diff([3, 5, 7, 2]))

# ---------------------------------------------------------------------

# Challenge 5
# Sum between range values
# You are given an array of integers and two integer values, min and max.
# Your task is to write a function that finds the sum of all elements in the
# array that fall within the range [min, max], inclusive.
#
# Example:
# arr = [3, 2, 1, 4, 10, 8, 7, 6, 9, 5]
# min_val = 3
# max_val = 7
#
# Output: 25 (3 + 4 + 5 + 6 + 7)
#
# Hint:  Iterate through each number (num) in the array (arr) and check if the current number  falls within the range [min_val, max_val].

def sum_between_range(arr, min_val, max_val):
# Your code here
    total_sum = 0
    for num in arr:
        if min_val <= num <= max_val:
            total_sum += num
    return total_sum



print(sum_between_range([3, 2, 1, 4, 10, 8, 7, 6, 9, 5], min_val = 3, max_val = 7))