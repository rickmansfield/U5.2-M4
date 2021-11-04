# Unit 5.2 M4 Task 4

# Question
- Below is an example implementation of the binary search algorithim in python.
- What must be true for this algorithm to work? 
```python
def binary_search(item_list, item):
    first = 0 
    last = len(item_list) - 1
    while first <= last:
        mid = first + (last - first) // 2
        if item_list[mid] == item :
            return True
        else: 
            if item < item_list[mid]:
                last = mid -1
            else: 
                first = mid + 1
    return False
```

# Answers
- item_list must be sorted (direction does not matter)
- item_list must have an even number of elements
- item_list must be sorted from smallest to greatest
- item_list must have more than two elements

# Solution