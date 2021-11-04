def csSearchRotatedSortedArray(nums, target):
    min = 0
    max = len(nums) - 1

    while not max < min:
        speculation = (max + min) // 2
        if nums[speculation] == target:
            return speculation
        elif nums[min] <= nums[speculation]:
            if nums[min] <= target < nums[speculation]:
                max = speculation
            else:
                min = speculation + 1
        else:
            print('min is greater than or equal to speculation')
            if nums[max - 1] >= target > nums[speculation]:
                min = speculation + 1
            else:
                max = speculation

    return -1
