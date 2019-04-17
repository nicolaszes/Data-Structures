# sqrt(y) 开平方根
# 二分法
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1: return x
        l, r = 0, 50000 # 50,000 is roughly the square root of 2^31 and is the upper

        while l <= r:
            m = (l + r) // 2
            m_2 = m * m # 增加内存开销，节省计算时间？

            if m_2 == x:
                return m
            elif m_2 > x:
                r = m - 1
            else:
                l = m + 1
        return l - 1
        # l, r = 0, 50000 # 50,000 is roughly the square root of 2^31 and is the upper
        # while l < r:
	    #     mid = (l + r) // 2
	    #     mid_2 = mid * mid
	    #     if mid_2 < x:
		#         l = mid + 1
	    #     else:
		#         r = mid
        # return l if l * l <= x else l - 1

# 牛顿迭代法
class Solution(object):
    def mySqrt(self, x):
        r = x
        while r * r > x:
            r = (r + x / r) / 2
        print(r)
        return r
