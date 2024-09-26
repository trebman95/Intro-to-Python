# Exercise 5: Movie Night Decision
# You and your friends are deciding on a movie to watch. Write a
# program that takes two movie ratings as input. If both ratings
# are above 7, print "Let's watch both!". Otherwise,
# print "Let's just pick one."
first_rating = int(input("Enter first movie rating: "))
second_rating = int(input("Enter second movie rating: "))

if first_rating > 7 and second_rating > 7:
    print("Let's watch both!")
else:
    print("Let's just pick one.")




