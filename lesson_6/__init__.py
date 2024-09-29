# Exercise 3. The Steps Tracker 👟

# Walking is a great way to improve one's health, and it can be fun!
# Doctors recommend 10,000 steps per day! You would like to know how many steps are YOU taking per day and per week.

# Write a program that will ask you the number of steps taken each day of the week, for one week.
# The program should put the step counts in a list, where index 0 is the number for Monday,
# index 1 is the number for Tuesday, and so on.

# Once you have all the steps counts, answer the following questions:
# - How many steps you took on Wednesday?
# - How many steps you took on the work days (Mon - Fri)?
# - How many steps total did you take over the whole week?
# - What was the least number of steps you took on a day?
# - What was the most number of steps you took on a day?

monday = input('Steps for Monday: ')
tuesday = input('Steps for Tuesday: ')
wednesday = input('Steps for Wednesday: ')
thursday = input('Steps for Thursday: ')
friday = input('Steps for Friday: ')
saturday = input('Steps for Saturday: ')
sunday = input('Steps for Sunday: ')

steps = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]

# Steps on Wednesday
print(f'Steps on Wednesday is {steps[2]}')

# Steps on the work days
work_days_steps = steps[0:5]
print({sum(work_days_steps)})

# Steps over the whole week
print(f'Steps over the whole week is {sum(steps)}')

# Least number of steps
print(f'Least number of steps is {min(steps)}')

# Highest number of steps
print(f'Highest number of steps is {max(steps)}')