class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []

        nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):
            # 如果出现最小元素为正数，则不存在和为0的情况，直接返回
            if nums[k] > 0:
                break
            # 如果出现第一个元素重复的情况，为避免重复结果，跳过后续执行
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            # 定义接下来的两个元素的双指针
            i, j = k + 1, len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    # 跳过重复元素
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    # 跳过重复元素
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    # 当出现元素满足条件是，将结果加入到列表
                    res.append([nums[k], nums[i], nums[j]])
                    # 接着更新索引（注意跳过相同元素）
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return res