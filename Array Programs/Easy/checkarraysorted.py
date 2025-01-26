# Python program to check whether the array is sorted or not

# ---- using loop ----- #
def is_sorted(nums) -> bool:
    for i in range(1,len(nums)):
        if nums[i-1] > nums[i]:
            return False
    return True

lst = [1,2,3,4,5,3]
res = is_sorted(lst)
print(res)

# ---- using all ----- #
def is_sorted(nums):
    return all(nums[i-1] <= nums[i] for i in range(1,len(nums)))

lst = [1,2,3,4,5]
res = is_sorted(lst)
print(res)

# ---- using all and zip ----- #
def is_sorted(nums):
    return all(x<=y for x,y in zip(nums,nums[1:]))

lst = [1,2,3,4,5]
res = is_sorted(lst)
print(res)

def is_sorted(nums) -> bool:
    return nums == sorted(nums)

lst = [1, 2, 3, 4, 5, 3]
res = is_sorted(lst)
print(res)

from functools import reduce

def is_sorted(nums) -> bool:
    return reduce(lambda x, y: x and y >= x, nums[1:], True)

lst = [1, 2, 3, 4, 5, 3]
res = is_sorted(lst)
print(res)


# Time and Space Complexities:
# Method 1: Time Complexity: O(n), Space Complexity: O(1)
# Method 2: Time Complexity: O(n), Space Complexity: O(1)
# Method 3: Time Complexity: O(n), Space Complexity: O(n)
# Method 4: Time Complexity: O(n log n) (due to sorted()), Space Complexity: O(n)
# Method 5: Time Complexity: O(n), Space Complexity: O(1)