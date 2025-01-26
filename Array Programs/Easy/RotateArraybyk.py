# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

def rotate_array(nums,k): #1,2,3,4,5
    k = k%len(nums)
    l,r = 0,len(nums)-1
    while l < r:
        nums[l],nums[r] = nums[r],nums[l]
        l,r = l+1,r-1  #5,4,3,2,1

    l,r = 0,k-1
    while l < r:
        nums[l],nums[r] = nums[r],nums[l]
        l,r = l+1,r-1  #4,5,3,2,1

    l,r = k,len(nums)-1
    while l<r:
        nums[l],nums[r] = nums[r],nums[l]
        l,r = l+1,r-1  #4,5,1,2,3

    return nums

lst = [1,2,3,4,5]
k = 2
res = rotate_array(lst,k)
print(res)

    
from collections import deque

def rotate_array_reverse(nums, k):
    """Rotation using the reversal algorithm."""
    k = k % len(nums)
    # Reverse the whole array
    nums.reverse()
    # Reverse the first k elements
    nums[:k] = reversed(nums[:k])
    # Reverse the rest of the array
    nums[k:] = reversed(nums[k:])
    return nums

def rotate_array_slicing(nums, k):
    """Rotation using slicing."""
    k = k % len(nums)
    return nums[-k:] + nums[:-k]

def rotate_array_deque(nums, k):
    """Rotation using deque."""
    dq = deque(nums)
    dq.rotate(k)  # Positive k rotates to the right, negative k to the left
    return list(dq)

# Input array and rotation value
lst = [1, 2, 3, 4, 5]
k = 2

# Method 1: Reversal Algorithm
lst1 = lst[:]  # Copy of the list to avoid modifying the original
print("Reversal Algorithm:", rotate_array_reverse(lst1, k))

# Method 2: Slicing
lst2 = lst[:]  # Copy of the list
print("Slicing Method:", rotate_array_slicing(lst2, k))

# Method 3: Using deque
lst3 = lst[:]  # Copy of the list
print("Deque Method:", rotate_array_deque(lst3, k))

