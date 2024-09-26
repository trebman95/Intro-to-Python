# Create a variable called number. Set it to any integer.
number = int(input('Enter an integer: '))
# If the number is divisible by 3, print 'Fizz'
# If the number is divisible by 5, print 'Buzz'
# If the number is divisible by both 3 and 5, print 'FizzBuzz'

#if number // 3:
#    print('Fizz')
#    if number // 5:
#       print('Buzz')
#       if number // 3 and number // 5:
#          print('FizzBuzz')

if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')


