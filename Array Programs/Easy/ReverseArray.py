# 3. Reverse an array

# ----- slcing method ------ #
def reverse_array(arr):
    return arr[::-1]

# Example Usage
arr = [1, 2, 3, 4, 5]
reversed_arr = reverse_array(arr)
print(reversed_arr)  # Output: [5, 4, 3, 2, 1]

# ----- reverse method ------ #
def reverse_array(arr):
    arr.reverse()

# Example Usage
arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print(arr)  # Output: [5, 4, 3, 2, 1]

# ----- swapping method ------ #
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # Swap
        left += 1
        right -= 1

# Example Usage
arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print(arr)  # Output: [5, 4, 3, 2, 1]

# -------- recursive way ---------
def reverse_array(arr):
    if len(arr) == 0:
        return arr
    else:
        return [arr[-1]] + reverse_array(arr[:-1])

# Example Usage
arr = [1, 2, 3, 4, 5]
reversed_arr = reverse_array(arr)
print(reversed_arr)  # Output: [5, 4, 3, 2, 1]

# ----- Iterative way method ------ #
def reverse_array(lst):
    for i in range(len(lst)-1,-1,-1):
        print(lst[i],end=" ")

lst = [1,2,3,4,5]
reverse_array(lst)

# ------ reversed method ------ #
def reverse_array(arr):
    return list(reversed(arr))

# Example Usage
arr = [1, 2, 3, 4, 5]
reversed_arr = reverse_array(arr)
print(reversed_arr)  # Output: [5, 4, 3, 2, 1]

# using stack datastructure
def reverse_array(arr):
    stack = []
    for element in arr:
        stack.append(element)
    
    reversed_arr = []
    while stack:
        reversed_arr.append(stack.pop())
    
    return reversed_arr

# Example Usage
arr = [1, 2, 3, 4, 5]
reversed_arr = reverse_array(arr)
print(reversed_arr)  # Output: [5, 4, 3, 2, 1]

# temporary array
def reverse_array(arr):
    n = len(arr)
    reversed_arr = [0] * n  # Initialize a temporary array of the same length
    for i in range(n):
        reversed_arr[i] = arr[n - 1 - i]
    return reversed_arr

# Example Usage
arr = [1, 2, 3, 4, 5]
reversed_arr = reverse_array(arr)
print(reversed_arr)  # Output: [5, 4, 3, 2, 1]

def reverse_array(lst):
    if len(lst) == 0:
        return lst
    return [lst[-1]] + reverse_array(lst[:-1])

lst = [5,4,3,2,1]
print(reverse_array(lst))
