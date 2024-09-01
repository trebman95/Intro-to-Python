# We are building a text formatting tool that assists users
# in refining the presentation of their text. The tool
# offers convenient options to modify the text's case and
# style without manual editing.

# Given the user's input:
text = input("Enter the text to be formatted: ")

# Format this "text" variable so you can show the variable in:
# - uppercase
# - lowercase
# - with the first letter of each word capitalized and the rest
#   of the letters in lowercase
# - total length of the string.

# Example:
# Enter text to be formatted: hello wORLD

# Expected output:
# Uppercase: HELLO WORLD
print('Uppercase: ' + text.upper())
# Lowercase: hello world
print('Lowercase: ' + text.lower() )
# Title: Hello World
print('Title: ' + text.title())
# Length: 11
print('Length: ' + str(len(text)))
