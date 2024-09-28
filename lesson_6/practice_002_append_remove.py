# Create an empty list and add the following elements about your location, in this order:
# - City
# - State or Province
# - A list with the temperatures the last three days
# - Your favorite animal

my_list = []
my_list.append('Charlotte')
my_list.append('North Carolina')
my_list.append([65, 72, 54])
my_list.append('Lion')

# Then, remove the State, without using the indexes.
my_list.remove('North Carolina')

# Bonus: Remove the last element, using a negative index.
del my_list[-1]

print(my_list)
