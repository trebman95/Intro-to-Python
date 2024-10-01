# Given a number, print its factorial.

number = int(input('Enter a number: '))
result = 1

for i in range(2, number + 1):
    result *= i

print(f'Factorial of {number} is {result}')

