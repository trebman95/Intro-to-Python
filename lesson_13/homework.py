# Homework Lesson 13 - Workshop - Homework

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

################################################################################
### When solving coding challenges, think about the time complexity (Big O). ###
################################################################################

# Challenge 1
# Common Elements Finder

# Given two lists of integers, find and return a new list containing elements that appear in both lists.
# Make sure the resulting list does not contain duplicates.

# Example:

# Input:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
# Output: [4, 5]

# Hints:
# You'll need to use nested loops: The outer loop will iterate over elements in the first list,
# and the inner loop will check if that element exists in the second list.
# Keep track of the common elements found so far to ensure no duplicates are added to the resulting list.
# To ensure no duplicates are added to the resulting list,
# check if an element is already present in the "common" list before appending it.

def find_common_elements(list1, list2):
    common = []

    for item1 in list1:
        for item2 in list2:
            if item1 == item2 and item1 not in common:
                common.append(item1)
                break

    return common

print(find_common_elements(list1, list2))

# ---------------------------------------------------------------------

# Refresher
# One of the key skills during job interviews
# is to be able to modify the code you've created.
# The following two tasks are the extension of the recipe problem you solved in class.

# Let's refresh the problem you solved in the class.
# You have a list of recipes, where each recipe contains the ingredients each recipe needs:
# recipes = [
# ["yeast","flour"],
# ["bread","meat"],
# ["flour","meat"]
# ]

# Solution

def find_makeable_recipes(recipes, ingredients):
    makeable_recipes = []
    for recipe in recipes:
        can_make = True
        for ingredient in recipe:
            if ingredient not in ingredients:
                can_make = False
                break
        if can_make:
            makeable_recipes.append(recipe)
    return makeable_recipes


test_recipes = [["yeast", "flour"], ["bread", "meat"], ["flour", "meat"]]
test_ingredients = ["yeast", "flour", "meat"]
test_result = find_makeable_recipes(test_recipes, test_ingredients)
print(test_result)


# ---------------------------------------------------------------------

# Challenge 2
# Missing ingredients

# You have a new list of recipes and ingredients.

# recipes = [
# ["yeast", "flour"],
# ["bread", "meat", "flour"]
# ]

# ingredients = ["yeast","bread"]

# Return the list of missing ingredients for all the recipes.

# Output: ["flour","meat"]


def find_missing_ingredients(recipes, ingredients):
    missing_ingredients = [] # Create an empty list to store the missing ingredients

    for recipe in recipes: # In the outer loop iterate through each recipe in the list of recipes.
        for ingredient in recipe: # In the inner loop check each ingredient in the recipe.
            if ingredient not in ingredients: # In the inner loop check each ingredient in the recipe.
                if ingredient not in missing_ingredients: #Check if the ingredient is not in the missing ingredients
                    missing_ingredients.append(ingredient) # If both conditions are met, add the ingredient to the  list

    return missing_ingredients # Return the list of missing ingredients required for all the recipes.


# ---------------------------------------------------------------------

# Challenge 3
# The best recipe
from typing import List

# You have a new list of recipes, where each recipe contains the ingredients it needs.

recipes = [
  ["yeast","flour"],
  ["bread","meat"],
  ["flour","meat", "yeast"]
 ]


# You also have a list of available ingredients.
ingredients = ["yeast","flour", "meat", "salt"]

# Return the list of the best recipe (the one that uses most of ingredients).

# Output: ["flour","meat", "yeast"]

def find_best_recipe(recipes, ingredients):
# Initialize variables to remember the best recipe and the most ingredients used.
    best_recipe = None
    max_used_ingredients = 0

    for recipe in recipes: # Create an outer for loop to go through each recipe in the list of recipes.
        used_ingredients = [] # Create an empty list (used_ingredients) to store the ingredients.
        for ingredient in recipe: # Create an inner for loop to look at each ingredient in this recipe.
            if ingredient in ingredients: # if the ingredient is in our list of available ingredients.
                used_ingredients.append(ingredient) # If it's available, add it to our list of used ingredients.
        if len(used_ingredients) > max_used_ingredients: # Check if the current recipe uses more ingredients
            max_used_ingredients = len(used_ingredients) # If ingredient count is higher, update max_used_ingredients.
            best_recipe = recipe # Then set this recipe as the new best.

    return best_recipe  # Finally, return the best recipe that uses the most ingredients.


    # Define the list of recipes and available ingredients.

    # Call the function to find the best recipe and print the result.

print(find_best_recipe(recipes,ingredients))


# ---------------------------------------------------------------------

# Challenge 4
# Find a peak element
# You are given an array of integers, and your goal is to find a "peak" element in the array.
# A peak element is an element that is strictly greater than its adjacent elements (elements on the left and on the right).

# Write a Python function find_peak_element(arr) that takes an array of integers as input
# and returns the index of the peak element in the array.

# Handle edge cases:
# - If the array has fewer than three elements, return -1.

# Check each element in the array:

# - If an element is strictly greater than both its adjacent elements (if they exist), consider it a peak element.
# - Return the index of the first peak element you find.
# - If no peak elements are found, return -1.

# Example:
arr1 = [1, 3, 20, 4, 1, 0]
# result1 = find_peak_element(arr1)
# print(result1)  # Output: 2 (Peak element: 20)

arr2 = [1, 2, 3, 4, 5]
# result2 = find_peak_element(arr2)
# print(result2)  # Output: -1 (No peak elements)

arr3 = [5, 10, 20, 15]
# result3 = find_peak_element(arr3)
# print(result3)  # Output: 2 (Peak element: 20)

def find_peak_element(arr):
    n = len(arr) # Find out how many elements are in the array

    if n < 3: # Check for the edge case (less than 3 elements)
        return -1

    if arr[0] > arr[1]: # Check the first and last element separately as they don't have neighbors
        return 0

    if arr[n - 1] > arr[n - 2]:
        return n - 1

    for i in range(1, n - 1): # Iterate over the range, excluding the first & last indices, as they lack one neighbor.
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            return i

    return -1 # Return -1 # if no peak element is found.


print(find_peak_element(arr1))
print(find_peak_element(arr2))
print(find_peak_element(arr3))

# ---------------------------------------------------------------------

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