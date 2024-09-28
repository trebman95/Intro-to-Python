# Given an integer, return the integer with reversed digits.
#
# Note:
# The integer could be either positive or negative.
#
# Example:
# -876 -> -678

original_int = int(input("Enter an integer: "))

if original_int < 0:
    reversed_int = int("-" + str(abs(original_int))[::-1])
else:
    reversed_int =int(str(original_int[::-1]))

print(reversed_int)
