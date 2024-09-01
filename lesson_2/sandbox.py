number = 1597

#digit_1 = number % 10
#digit_2 = (int(number % 100 / 10))
#digit_3 = (int(number % 1000/ 100))
#digit_4 = (int(number % 10000/ 1000))

#print(digit_1)
#print(digit_2)
#print(digit_3)
#print(digit_4)

digit_1 = number % 10
number = number // 10

digit_2 = number % 10
number = number // 10

digit_3 = number % 10
number = number // 10

digit_4 = number % 10
number = number // 10

print(digit_1)
print(digit_2)
print(digit_3)
print(digit_4)