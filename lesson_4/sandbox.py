# Exercise 7: Exercise 7: Tax Bracket Calculator
# You're building a tax calculation system. Write a program that
# takes a person's annual income as input. Use conditionals
# to determine their tax bracket based on the following rules:
from lesson_4.homework import tax_amount

# - If income is less than $40,000, tax rate is 10%.
# - If income is between $40,000 and $100,000 (inclusive), tax rate is 20%.
# - If income is greater than $100,000, tax rate is 30%.

# Remember that a tax rate of 10% can be represented as 10/100 or 0.1

# Print the calculated tax amount for the given income.
annual_income = float(input("Enter your annual income: "))

# <Your code here>
if annual_income < 40000:
    tax_rate = 0.1
elif 40000 <= annual_income <= 100000:
    tax_rate = 0.2
else:
    tax_rate = 0.3

tax_amount = annual_income * tax_rate

# Print tax amount
print(f"Your tax amount is ${tax_amount}")