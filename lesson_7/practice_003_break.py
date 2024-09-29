# We would like to make a program that prints the first
# three fruits that DO NOT contain the letter "d" in their name.

fruits = [
   "apple", "banana", "cherry", "grape",
   "orange", "blueberry", "blackberry",
   "kiwi", "pear", "strawberry"
]

# We should have some way to track how many we’ve found.
found = 0

for fruit in fruits:
   if "d" not in fruit:
       print(f"{fruit} does not have the letter D in its name.")
       found =+ 1

   if found == 3:
       break