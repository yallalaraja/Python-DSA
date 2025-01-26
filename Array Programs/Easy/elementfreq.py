from collections import Counter
import numpy as np

# Method 1: Using Dictionary
def frequency_dict(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return freq

# Method 2: Using collections.Counter
def frequency_counter(nums):
    return Counter(nums)

# Method 3: Using count() Method
def frequency_count_method(nums):
    freq = {}
    for num in set(nums):
        freq[num] = nums.count(num)
    return freq

# Method 4: Using Sorting and Iteration
def frequency_sorted(nums):
    nums.sort()
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return freq

# Method 5: Using NumPy
def frequency_numpy(nums):
    unique, counts = np.unique(nums, return_counts=True)
    return dict(zip(unique, counts))

# Input list
lst = [1, 2, 2, 3, 4, 4, 4, 5]

# Testing all methods
print("Frequency using Dictionary:", frequency_dict(lst))
print("Frequency using Counter:", frequency_counter(lst))
print("Frequency using count():", frequency_count_method(lst))
print("Frequency using Sorting:", frequency_sorted(lst[:]))  # Pass a copy since sorting modifies the list
print("Frequency using NumPy:", frequency_numpy(lst))

# Method	Time Complexity	Space Complexity
# Dictionary	O(n)	O(n)
# collections.Counter	O(n)	O(n)
# count() Method	O(n^2)	O(n)
# Sorting + Iteration	O(n log n)	O(n)
# NumPy	O(n log n)	O(n)