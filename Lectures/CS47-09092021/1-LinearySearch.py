# Linear Search
"""
iterate over each element in `lst` using a range based loop
  check if the current element is equal to the `target`
    return the index of the element
  
return negative one if we get here
"""


def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i

    return -1


l = [23, 34, 12, 3, 5654, 2, 14, 456]

print(linear_search(l, 23))
print(linear_search(l, 456))
print(linear_search(l, 9876))
