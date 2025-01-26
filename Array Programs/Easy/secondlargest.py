# Find the Second Largest Element in an Array

def second_largest(nums:list) -> int:
    first_max = nums[0]
    second_max = nums[0] 

    for i in range(len(nums)):
        if nums[i] > first_max:
            second_max = first_max
            first_max = nums[i]

        if nums[i] > second_max and nums[i]!=first_max:
            second_max = nums[i]

    return second_max

lst = [1,2,3,4,5]
res = second_largest(lst)
print(res)

import heapq

def second_largest_sort(nums):
    """Find second largest using sorting."""
    nums = list(set(nums))  # Remove duplicates
    if len(nums) < 2:
        return None  # Not enough elements for second largest
    nums.sort()  # Sorting the list
    return nums[-2]

def second_largest_single_pass(nums):
    """Find second largest using a single pass."""
    if len(nums) < 2:
        return None  # Not enough elements for second largest
    
    largest = second = float('-inf')
    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    
    return second if second != float('-inf') else None

def second_largest_heap(nums):
    """Find second largest using heapq."""
    if len(nums) < 2:
        return None  # Not enough elements for second largest
    nums = list(set(nums))  # Remove duplicates
    return heapq.nlargest(2, nums)[-1] if len(nums) >= 2 else None

# Input list
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Using Sorting
print("Second Largest (Sort):", second_largest_sort(nums))
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(n) due to list and set operations

# Using Single Pass
print("Second Largest (Single Pass):", second_largest_single_pass(nums))
# Time Complexity: O(n), where n is the number of elements in the list
# Space Complexity: O(1), constant space for largest and second variables

# Using Heap
print("Second Largest (Heap):", second_largest_heap(nums))
# Time Complexity: O(n log k), where k = 2 (for the 2 largest elements, so O(n))
# Space Complexity: O(n) for storing unique elements in the set
