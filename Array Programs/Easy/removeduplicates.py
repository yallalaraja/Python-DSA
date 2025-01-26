# To remove duplicates from a sorted array in Python, you can use a two-pointer approach.

from itertools import groupby

def remove_duplicates_two_pointer(nums):
    if not nums:
        return 0

    unique_index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[unique_index] = nums[i]
            unique_index += 1
    return unique_index

def remove_duplicates_set(nums):
    nums[:] = sorted(set(nums))
    return len(nums)

def remove_duplicates_list_comprehension(nums):
    nums[:] = [nums[i] for i in range(len(nums)) if i == 0 or nums[i] != nums[i - 1]]
    return len(nums)

def remove_duplicates_temp_list(nums):
    unique_nums = []
    for num in nums:
        if not unique_nums or num != unique_nums[-1]:
            unique_nums.append(num)
    nums[:] = unique_nums
    return len(nums)

def remove_duplicates_groupby(nums):
    nums[:] = [key for key, _ in groupby(nums)]
    return len(nums)

# Test the methods
nums = [1, 1, 2, 2, 3, 4, 4, 5]

# Two-pointer method
nums_copy = nums[:]
new_length = remove_duplicates_two_pointer(nums_copy)
print("Two-pointer method:")
print(f"Array after removing duplicates: {nums_copy[:new_length]}")
print(f"New length of the array: {new_length}\n")

# Using set()
nums_copy = nums[:]
new_length = remove_duplicates_set(nums_copy)
print("Using set():")
print(f"Array after removing duplicates: {nums_copy}")
print(f"New length of the array: {new_length}\n")

# List comprehension
nums_copy = nums[:]
new_length = remove_duplicates_list_comprehension(nums_copy)
print("List comprehension:")
print(f"Array after removing duplicates: {nums_copy}")
print(f"New length of the array: {new_length}\n")

# Temporary list
nums_copy = nums[:]
new_length = remove_duplicates_temp_list(nums_copy)
print("Using a temporary list:")
print(f"Array after removing duplicates: {nums_copy}")
print(f"New length of the array: {new_length}\n")

# Using itertools.groupby
nums_copy = nums[:]
new_length = remove_duplicates_groupby(nums_copy)
print("Using itertools.groupby:")
print(f"Array after removing duplicates: {nums_copy}")
print(f"New length of the array: {new_length}\n")

