"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

for example:    
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    if type(nums) != list:
        print('nums type should be a list')
        return;
    if type(target) != int:
        print('target type should be a int')
        return

    """
    for loop the nums element
    get the number(n) equal to target minus m
    """
    for m in nums:
        n = target - m

        """
        # when nums have n, run the code below
        # if n equal to m and nums have more than one n element
        # if n not equal to m
        """
        if n in nums:

            if n == m and nums.count(n) > 1:
                mIndex = nums.index(m)
                # in order to get the next n index
                # i got to remove the first one
                # sorry can not find the best way to do it
                nums.remove(m)
                nIndex = nums.index(n) + 1
                return [mIndex, nIndex]
            elif n != m:
                mIndex = nums.index(m)
                nIndex = nums.index(n)
                return [mIndex, nIndex]
        else:
            continue

twoSum([], [2, 5, 5, 11], 10)
