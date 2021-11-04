# Binary Search
"""

- set a min value to zero
- set a max value to the length of the data minus 1

- keep iterating over the data while min is lessthan or equal to max
  - create a guess_index by adding min and max together and floor dividing them
  - test if the data at the index of guess_index is equal to the target
    - return the guess_index
  - otherwise test if data at the guess_index is less than the target
    - set the min to guess_index + 1
  - otherwise
    - set the max to the guess_index - 1

- return -1 to the caller

"""


from time import time


def binary_search(lst, target):
    min = 0
    max = len(lst) - 1

    while min <= max:
        guess_index = (min + max) // 2

        if lst[guess_index] == target:
            return guess_index

        elif lst[guess_index] < target:
            # go to the right
            min = guess_index + 1
        else:
            # go to the left
            max = guess_index - 1

    return -1


def binary_search_r(lst, min, max, target):
    if min <= max:
        guess_index = (min + max) // 2

        # base case
        if lst[guess_index] == target:
            return guess_index

        elif lst[guess_index] < target:
            # go to the right
            return binary_search_r(lst, guess_index + 1, max, target)
        else:
            # go to the left
            return binary_search_r(lst, min, guess_index - 1, target)
    else:
        # base case
        return -1


l = ["Dave", "Edd", "Frank", "Gabe", "Harris", "Hugo", "Joe", "Kelly", "Zoe"]
start = time()
print(binary_search(l, "Hugo"))
end = time()
print("linear", end - start)
print("====================")
start = time()
print(binary_search_r(l, 0, len(l), "Hugo"))
end = time()
print("recursive", end - start)
