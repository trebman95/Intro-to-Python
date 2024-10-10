# Given an array of integers, write a function to move all 0's
# to the end while maintaining the relative order of the other elements.
# Input: 0 4 0 3 12
# Output: 4 3 12 0 0

def move_zeros(arr):
# Your code here
# Index to keep track of the position for non-zero elements
    non_zero_pos = 0

# Traverse the array, moving non-zero elements to the front
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_pos] = arr[i]
            non_zero_pos += 1

# Fill the remaining positions with zeros
    for i in range(non_zero_pos, len(arr)):
        arr[i] = 0

    return arr

# Test case
arr = [0, 4, 0, 3, 12]
print(move_zeros(arr))  # Output: [4, 3, 12, 0, 0]