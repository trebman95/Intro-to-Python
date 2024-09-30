# Given a list.
# Calculate sum and multiplication of all elements.
# Print the list, sum and multiplication of elements.
# For example:
# Input: [1, 2, 3, 4]
# Output sum: 10
# Output multiplication: 24


numbers = [1, 2, 3, 4]
sum_result = 0
mult_result = 1

for number in numbers:
    sum_result = sum_result + number
    mult_result = mult_result * number

print(numbers)
print(f'Output sum: {sum_result}')
print(f'Output mult: {mult_result}')



