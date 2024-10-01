# Your goal is to write a Python program that finds the maximum number in a given list of numbers.
# Example:
numbers = [1, 2, 42, 77, 99, -100]
# Output: 99

result = numbers[0]

for number in numbers:
    if number > result:
        result = number
# numbers.sort()

print(result)
# print(numbers[-1])