# 1.Find the largest element in an array.

def large_element(lst):
    max_elem = lst[0]
    for elem in lst:
        if elem > max_elem:
            max_elem = elem
    return max_elem

lst = [1,2,3,4,5,6,8,2]
res = large_element(lst)
print(f"Largest element is {res}")