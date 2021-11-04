def csSearchRotatedSortedArray(nums, target):
    min = 0
    max = len(nums) - 1

    while not max < min:
        guess = (max + min) // 2
        # print(f'min: {nums[min]} max: {nums[max]} guess:{nums[guess]} target:'
        #       f' {target}')
        # if the guess is the target we got it and return the guess
        if nums[guess] == target:
            # print('guessed the target')
            return guess
        # if min is less than or equal to the guess
        elif nums[min] <= nums[guess]:
            # print('min less than guess')
            # if min is less than or equal to the target and less than the guess
            if nums[min] <= target < nums[guess]:
                # print('min less than or equal to target and less than guess')
                # we can set max to the guess because nothing past the guess
                # can be the target
                max = guess
                # else we can set min to guess + 1 because nothing before it
                # can be the target
            else:
                # print('min is greater than target and greater than or equal '
                #       'to guess')
                min = guess + 1
        # else if min is greater than the guess
        else:
            print('min is greater than or equal to guess')
            # if max - 1 is greater than the target and greater than the guess
            if nums[max - 1] >= target > nums[guess]:
                # print('max - 1 greater than or equal to target and greater '
                #       'than guess')
                # we can set min to guess plus one because nothing before it
                # can be the target
                min = guess + 1
            else:
                # print('max -1 less than target and less than or equal to guess')
                # else we set max equal to guess because nothing after it can
                # be the target
                max = guess

    return -1
