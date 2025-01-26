from collections import deque

# Method 1: Brute Force
def is_subarray_brute_force(arr, subarr):
    n, m = len(arr), len(subarr)
    for i in range(n - m + 1):
        if arr[i:i + m] == subarr:
            return True
    return False

# Method 2: String Conversion
def is_subarray_str_conversion(arr, subarr):
    arr_str = ','.join(map(str, arr))
    subarr_str = ','.join(map(str, subarr))
    return subarr_str in arr_str

# Method 3: Sliding Window
def is_subarray_sliding_window(arr, subarr):
    n, m = len(arr), len(subarr)
    for i in range(n - m + 1):
        if all(arr[i + j] == subarr[j] for j in range(m)):
            return True
    return False

# Method 4: Using deque
def is_subarray_deque(arr, subarr):
    dq = deque(arr[:len(subarr)])
    for i in range(len(arr) - len(subarr) + 1):
        if list(dq) == subarr:
            return True
        if i + len(subarr) < len(arr):
            dq.popleft()
            dq.append(arr[i + len(subarr)])
    return False

# Input Arrays
arr = [1, 2, 3, 4, 5]
subarr = [3, 4]

# Test Each Method
print("Brute Force:", is_subarray_brute_force(arr, subarr))
print("String Conversion:", is_subarray_str_conversion(arr, subarr))
print("Sliding Window:", is_subarray_sliding_window(arr, subarr))
print("Deque Sliding:", is_subarray_deque(arr, subarr))
