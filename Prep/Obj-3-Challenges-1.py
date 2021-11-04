"""
# Unit 5.2 M4 prepwork Objective 3 challenge

Write a recursive search function that receives as input an array of integers and a target integer value. This function should return True if the target element exists in the array, and False otherwise.
What would be the base case(s) we'd have to consider for implementing this function?
How should our recursive solution converge on our base case(s)?
In your own words, write out the three rules for recursion and how you can identify when a problem is amenable to using a recursive method.
"""
def myBinarySearch(nums, target):
    if not nums:
        return -1
    start = 0
    end = len(nums) -1
    while start <= end:
        mid = start + end // 2
        if nums[mid] == target:
            return True
        elif target < nums[mid]:
            end = mid - 1
        else: 
            start = mid + 1
    return -1

print(myBinarySearch([1, 2, 3, 4, 5 , 6], 3))