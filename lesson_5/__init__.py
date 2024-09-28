# Challenge 5
# Reverse a string
#
# You're part of a team working on analyzing customer reviews for a new video game.
# Due to a software glitch, some reviews have been recorded in reverse with punctuation
# at the beginning instead of the end. Your task is to correct these reviews so that they
# are in the correct order and the punctuation is appropriately placed at the end of the
# sentence or word.
#
# Example: "tcefreP!" -> Perfect!

glitch_str = input("Enter you glitch word: ")
reversed_str = glitch_str[::-1]
corrected_str = ""

if reversed_str and reversed_str[0] in "!.,":
    corrected_str = reversed_str[1:] + reversed_str[0]
else:
    corrected_str = reversed_str


print(corrected_str)



