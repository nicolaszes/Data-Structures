class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 00010000...000 只有一个 1
        return n != 0 and (n & (n - 1) == 0)