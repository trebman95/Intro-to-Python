# Remove the lowercase vowels in a given string:
#str1 = 'Hello, World'
str1 = input('Enter a string: ')
# The vowels are:
vowels = "aeiou"
# “y” is not considered a vowel for this task. The input string is always in lowercase.
# Examples:
# "hello" --> "hll"
# "goodbye" --> "gdby"

result = ''

for string in str1:
    if string not in vowels:
        result += string

print(result)
