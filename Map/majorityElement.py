class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 暴力 O(N^2) 两层 for 循环
        
        # Map O(N) / O(N)
        # result = None
        # count = 0
        # for num in nums:
        #     if count == 0:
        #         result = num
        #     if result == num:
        #         count += 1
        #     else:
        #         count -= 1
        # return result
    
        # Sort O(NlogN)
        nums.sort()
        return nums[int(len(nums)/2)]

        # Divide & Conquer O(NlogN)