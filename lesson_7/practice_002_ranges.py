# Figure out the values required for range() to generate the expected result:

# 0, 1, 2, 3, 4
first = range(0, 5)
print(list(first))

# 20, 21, 22 ... 30 (all the numbers between 20 and 30, inclusive)
second = range(20, 31)
print(list(second))

# Even numbers: 2, 4, 6, 8, 10
third = range(2, 12, 2)
print(list(third))

# Years ending in zero between 1900 and 2000 (inclusive)
fourth = range(1900, 2001, 10)
print(list(fourth))

# Bonus!
# 20, 19, 18, 17, 16
fifth = range(20, 15, -1)
print(list(fifth))