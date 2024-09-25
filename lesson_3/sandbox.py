# Exercise 9: Workouts calculator
# Write a Python program that asks the user to input the number
# of minutes spent on three different exercises: cardio, strength
# training, and yoga using the input() function. Convert the input
# strings to integers using the int() function. Calculate the
# total time spent on workouts by summing up the minutes from all
# three activities. Based on the total workout time, provide a
# motivational message using an f-string that encourages the user
# to stay consistent and reach their fitness goals. Display the
# motivational message to the user.

cardio = int(input('Enter your minutes on cardio:'))
strength_training = int(input('Enter your minutes on strength training:'))
yoga = int(input('Enter your minutes on yoga:'))

total_time = cardio + strength_training + yoga

good_job = f'You have worked out for {total_time} minutes total, Keep it up!'

print(good_job)
