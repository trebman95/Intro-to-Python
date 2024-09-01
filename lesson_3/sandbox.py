# Exercise 6: Text Transformation Game
# Create a text transformation game. Ask the user
# to enter a sentence. Replace all vowels with '*'. Display the
# modified sentence.
#
# Example Input: "Hello, world!"
# Example Output: "H*ll*, w*rld!"
sentence = input("Enter a sentence: ")
vowel = 'a', 'e', 'i', 'o', 'u'
transformed_sentence = sentence.replace('aeiouAEIOU','*')
print(transformed_sentence)



