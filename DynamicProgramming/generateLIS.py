import math
'''
复杂度为O(N^2)的方法，算法很简单。
dp[i]表示在以arr[i]这个数结尾的情况下，arr[0....i]中的最大递增子序列
'''
def getdp1(arr):
    n = len(arr)
    dp = [0] * n
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if arr[i] > arr[j]:
                # 记录前面有多少个大于当前 arr[i]的值，计作 dp[i]
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

def getdp2(arr):
    # 用一个数组ends保存，在所有长度为i的递增序列中，最小的结尾数为ends[i-1]
    # 初始化一个ends[]和一个int型right，并规定ends[0,…,right]为有效区，否则为无效区
    # 遍历arr，假设当前为i
    # 在ends的有效区从最左边开始找，找到大于arr[i]的数，则表示arr[i]结尾的最长递增序列长度=right+1
    # 最后还有修改ends对应的值为arr[i]，以便下次遍历
    n = len(arr)
    dp, ends = [0] * n, [0] * n
    ends[0], dp[0] = arr[0], 1
    right, l, r, m = 0, 0, 0, 0
    for i in range(1, n):
        l = 0
        r = right
        # 二分查找,若找不到则 ends[l或r] 是比 arr[i] 大而又最接近其的数
        # 若 arr[i] 比 ends 有效区的值都大，则 l = right+1
        while l <= r:
            m = math.floor((l + r) / 2)
            if arr[i] > ends[m]:
                l = m + 1
            else:
                r = m - 1
        right = max(right, l)
        ends[l] = arr[i]
        dp[i] = l + 1
    return dp

def generateLIS(arr, dp):
    # 找到当前这个 dp的最大值
    # 找到这个最大值所在的索引位置
    # 创建新的返回数组 lis，长度为 n
    # 此时 arr[index] 是当前这个数组的最大值
    print(dp)
    n = max(dp)
    index = dp.index(n)
    lis = [0] * n
    n -= 1
    lis[n] = arr[index]
    # 从右向左遍历数组 arr
    for i in range(index, 0 - 1, -1):
        # 如果 arr[i]比整个数组的最大值还要小，并且dp[i]恰好 = dp[index] - 1
        if arr[i] < arr[index] and dp[i] == dp[index] - 1:
            n -= 1
            lis[n] = arr[i]
            index = i
    return lis

arr = [1, 2, 4, 3, 5, 4, 6, 8, 9, 7]
# print(getdp1([1, 2, 4, 3, 5, 4, 6, 8, 9, 7]))
# print(len(getdp1([1, 2, 3])))
print(generateLIS(arr, getdp2(arr)))

