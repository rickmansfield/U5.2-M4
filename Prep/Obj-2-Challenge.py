"""
Rewrite the implementation of linear search below so that the algorithm searches from the end of the list to the beginning.
"""
def linear_search(arr, target):
    # loop through each item in the input array
    for idx in range(len(arr)):
        # check if the item at the current index is equal to the target
        if arr[idx] == target:
            # return the current index as the match
            return idx
    # if we were able to loop through the entire array, the target is not present
    return -1# Linear Search
"""
Here is the proposed U.P.E.R and solution below
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
