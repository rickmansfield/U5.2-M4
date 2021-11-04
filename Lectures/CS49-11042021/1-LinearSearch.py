# Linear Search
def linear_search(lst, target):  # O(n) Linear
    for i in range(len(lst)):  # O(n)
        if lst[i] == target:  # O(1)
            return i  # O(1)

    return -1  # O(1)


l = [23, 34, 12, 3, 5654, 2, 13, 456]

print(linear_search(l, 9876))
