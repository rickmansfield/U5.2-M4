# Binary Search

def binary_search(lst, target):
    min = 0
    max = len(lst) - 1

    while min <= max:
        guess = (min + max) // 2

        if lst[guess] == target:
            return guess
        elif lst[guess] < target:
            min = guess + 1
        else:
            max = guess - 1

    return -1


l = [1, 2, 3, 45, 67, 78, 98, 120, 200]

print(binary_search(l, 78))
