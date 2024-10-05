# Create a program, that takes a word input from the user, and prints out a
# dictionary showing the letter count for each letter in the word.

# Examples:
#   cat  -> {"c" : 1, "a" : 1, "t" : 1}
#   call -> {"c" : 1, "a" : 1, "l" : 2}

# Use as many of the following concepts as you can:
# - Functions
# - Dictionaries
# - Asking for user input
# - Loops

# Bonus: Keep asking for words until the user types "end" OR an empty word.

while True:
    word = input('Give me a word: ')

    if word == 'end' or word == '':
        break

    counter = {}

    for char in word:
        if char in counter.keys():
            counter[char] += 1
           #counter[char] = counter[char] + 1
        else:
            counter[char] = 1

    print(counter)