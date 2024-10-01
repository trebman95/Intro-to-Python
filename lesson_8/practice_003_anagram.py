# Given two words, check if both are anagrams.
# An anagram of a string is another string that contains the same characters, only the order
# of characters can be different.
# For example:
# is_anagram('cat', 'act') => should return True
# is_anagram('bus', 'sub') => should return True
# is_anagram('map', 'cap') => should return False

first_word = input('Enter first word: ')
second_word = input('Enter second word: ')

if len(first_word) != len(second_word):
    print(False)
elif sorted(first_word) == sorted(second_word):
    print(True)
else:
    print(False)

