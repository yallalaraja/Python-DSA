#2. Find the Smallest element in an array.

def small_element(lst):
    mini_elem = lst[0]
    for elem in lst:
        if elem < mini_elem:
            mini_elem = elem
    return mini_elem

lst = [1,2,3,4,5,6,8,2]
res = small_element(lst)
print(f"smallest element is {res}")