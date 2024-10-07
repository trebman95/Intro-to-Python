# Given an array of integers, nums, and an integer target, return two numbers such
# that they add up to target.
# Assume there’s only one unique pair of numbers that will sum up to the target and
# you may not use the same element twice.
# You can return the answer in any order.
# Example:
# Input: nums = [1, 2, 3, 7, 5], target = 10
# Output: [3, 7]

def two_sum(arr, target):
    if len(arr) < 2:
        return

    partner_dict = {}
    for num in arr:
        partner = target - num
        if partner in partner_dict:
            return [num, partner]
        else:
            partner_dict[num] = True


nums = [1, 2, 3, 7, 5]
target = 10
print(two_sum(nums, target))