# 4.sum of array elements

# Built-in sum() – Fast and efficient for most cases.
# For loop – Manual approach, gives you flexibility.
# For loop with indexes – Another manual approach using index-based iteration.
# reduce() – A functional programming approach, less common for this task but useful in more complex scenarios.
# List comprehension – Compact but can use extra memory.
# Recursion – Elegant but can be inefficient for large arrays due to stack depth.
# Generator expression – Efficient in terms of memory compared to list comprehension.
# NumPy's np.sum() – Efficient for large numerical arrays (requires NumPy).
# While loop – Another loop-based approach, offers flexibility.

import numpy as np
from functools import reduce
#  ----------- Built-in sum() ----------
def array_sum(arr):
    return sum(arr)

lst = [1,2,3,4,5]
res = array_sum(lst)
print(res)

#  ----------- For loop -----------
def array_sum(arr):
    total_sum = 0
    for num in arr:
        total_sum+=num
    return total_sum

lst = [1,2,3,4,5]
res = array_sum(lst)
print(res)

#  ----------- For loop with indexes -----------
def array_sum(arr):
    total_sum = 0
    for i in range(len(arr)):
        total_sum += arr[i]
    return total_sum

lst = [1,2,3,4,5]
res = array_sum(lst)
print(res)

#  ----------- Using reduce method -----------
def array_sum(arr):
    return reduce(lambda x,y:x+y,arr)

lst = [1,2,3,4,5]
res = array_sum(lst)
print(res)

#  --------- List comprehension -----------
def array_sum(arr):
    return sum([num for num in arr])

lst = [1,2,3,4,5]
res = array_sum(lst)
print(res)

# ---------- recursion ------------
def array_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum(arr[1:])

lst = [1,2,3,4,5]
res = array_sum(lst)
print(res)

# ---------- Generator expression -----------
def array_sum(arr):
    return sum(num for num in arr)

lst = [1,2,3,4,5]
res = array_sum(lst)
print(res)

# using numpy and while loop
def array_sum(arr):
    return np.sum(arr)

lst = [1,2,3,4,5]
res = array_sum(lst)
print(res)

def array_sum(arr):
    i = 0
    total = 0
    while i < len(arr):
        total += arr[i]
        i+=1
    return total

lst = [1,2,3,4,5]
res = array_sum(lst)
print(res)



