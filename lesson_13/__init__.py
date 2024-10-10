# Challenge 5 (optional)
# Delete duplicates in sorted lists

# Given a sorted list of integers, write a program that:

# - Removes all duplicate values from the list.
# - Shifts the unique values to the left to fill any emptied indices.
# - Fills the remaining rightmost indices with zeroes.
# - Returns the count of unique values in the list.

# - Example:
# Input: [1, 2, 2, 3, 4, 4, 4, 5]
# Output: [1, 2, 3, 4, 5, 0, 0, 0], 5 (5 unique values)

# Hints:
# - Sequential Comparison: Since the list is sorted, duplicates will always be adjacent to each other.
# Compare each element to the previous one to detect duplicates.
# - Updating in Place: You can modify the original list as you find unique numbers
# and move them to the correct position. Think of this position as where the next unique number should go.

def delete_duplicates(arr):
    # 'write_index' points to where the next unique element should be written.
        write_index = 1

    # Iterate over the list's length, starting from the second element because
    # the first element doesn't have a previous element to compare against.

        for i in range(1, len(arr)):
            if arr[write_index - 1] != arr[i]:
                arr[write_index] = arr[i] # Place the current element at the 'write_index' position.
                write_index += 1 # Then increment 'write_index' by 1 to prepare for the next unique element.

    # Once you have shifted all unique elements to the left,
    # fill the remaining positions in the list with zeroes.

        for i in range(write_index, len(arr)):
            arr[i] = 0

    # Compare the current element with its immediate previous element.
    # If they're different, it's not a duplicate.

    # Return the modified list for visualization and the count of unique elements.

        print(arr)
        return write_index

print(delete_duplicates([1, 2, 2, 3, 4, 4, 4, 5]))