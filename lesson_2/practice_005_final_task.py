# Create a program that will calculate your monthly expenses.
# Each expense amount is represented by a variable.

rent = 1200
utilities = 300
groceries = 450
entertainment = 200

# Calculate the total monthly expenses and determine the
# percentage of rent relative to the total expenses.

expenses = rent + utilities + groceries + entertainment
rentPercentage = int((rent / expenses) * 100)

print(expenses)
print(rentPercentage)

# Hint: to count the percentage of rent, count total monthly
# expenses first, then divide expenses for rent by the total
# expenses and multiply by 100.
# int = converts the specified value into an integer number
