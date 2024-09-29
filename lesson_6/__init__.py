# Task 7. Aggregators and Helpers

# Given a list of numbers, use helpers and aggregators to answer the questions:

# - What's the lowest number?
# - What's the highest number?
# - What's the sum of all the numbers in the list?
# - How many times is the number 9 in the list?
# - How many total elements are in the list?

numbers = [6, 34, 17, 9, 2, 11, 57, 9, 32]

# Lowest number
print(min(numbers))

# Highest number
print(max(numbers))

# Sum of everything
print(sum(numbers))

# Count number 9s
print(numbers.count(9))

# Total number of elements
print(len(numbers))