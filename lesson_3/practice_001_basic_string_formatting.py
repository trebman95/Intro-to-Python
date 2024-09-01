# Given the following variables:
name = "Emily"
age = 26
job_title = "QA Manager"

# For each practice, print the following message using
# the requested string formatting method:
# "Emily is a 26 years old QA manager of our company"
# Practice 1.1 - Using concatenation with +
print(name + ' is a ' + str(age)  + ' years old ' + job_title + ' of our company ')

# Practice 1.2 - Using .format()
print('{name} is a {age} years old {job_title} of our company'.format(name = 'Emily', age = 26,
job_title = 'QA Manager'))

# Practice 1.3 - Using f-strings
message = f'{name} is a {age} years old {job_title} of our company'
print(message)