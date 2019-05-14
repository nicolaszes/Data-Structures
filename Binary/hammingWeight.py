class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1. x % 2 -> count + 1 Time: O(32)
        rst = 0
        mask = 1

        for i in range(32):
            if n & mask:
                rst += 1
            mask = mask << 1
        return rst

        # 2. x = x & (x - 1) Time: 有多少个 1
        res = 0
        while n > 0:
            res += 1
            n = n & n - 1
        return res
        