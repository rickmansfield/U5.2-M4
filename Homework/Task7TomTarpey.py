def csSearchRotatedSortedArray(nums, target):
    if target > len(nums):
        return -1
    return target - nums[0]