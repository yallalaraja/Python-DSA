# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:

# Input: nums = [3,0,1]

# Output: 2

# Explanation:

# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

def missing_number(nums:list) -> int:
    res = len(nums)
    for i in range(len(nums)):
        res += i-nums[i]
    return res

lst = [3,0,1]
res = missing_number(lst)
print(res)


def missing_number_sum(nums: list) -> int:
    """Method 1: Using the sum of numbers (Mathematical Formula)"""
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def missing_number_xor(nums: list) -> int:
    """Method 2: Using XOR"""
    n = len(nums)
    xor_all = 0  # XOR of all numbers from 0 to n
    xor_nums = 0  # XOR of all numbers in the list
    for i in range(n + 1):
        xor_all ^= i
    for num in nums:
        xor_nums ^= num
    return xor_all ^ xor_nums

def missing_number_sort(nums: list) -> int:
    """Method 3: Sort and find the missing number"""
    nums.sort()
    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return len(nums)  # If no missing number before n, return n

def missing_number_in_place(nums: list) -> int:
    """Method 4: Using the modified given formula"""
    res = len(nums)
    for i in range(len(nums)):
        res += i - nums[i]
    return res

# Test the methods
lst = [3, 0, 1]

# Method 1: Using sum formula
res1 = missing_number_sum(lst)
print(f"Missing number using sum: {res1}")

# Method 2: Using XOR
res2 = missing_number_xor(lst)
print(f"Missing number using XOR: {res2}")

# Method 3: Using sort
res3 = missing_number_sort(lst)
print(f"Missing number using sort: {res3}")

# Method 4: Using in-place adjustment
res4 = missing_number_in_place(lst)
print(f"Missing number using in-place adjustment: {res4}")
