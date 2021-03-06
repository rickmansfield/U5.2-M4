def csBinarySearch(nums, target):
    if not nums:
        return -1
    start = 0
    end = len(nums)-1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target: 
            if mid == 0 or nums[mid-1] < target:
                return mid
            else:
                end = mid - 1 
        elif target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1
print(csBinarySearch([1, 2, 3, 4, 5 , 6], 3))
print(csBinarySearch( [-1, 0, 3, 5, 9, 12], 2))
print(csBinarySearch( [-1, 0, 3, 5, 9, 12], 9))