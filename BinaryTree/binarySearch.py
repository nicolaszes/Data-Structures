'''
    二分查找法
    binary search
'''
# 有序数组 arr查找 target
# 如果找到 target，返回相应的索引 index
# 如果找不到 target，返回 -1
def binarySearch (arr, n, target) :
    l = 0
    r = n - 1
    # 在 arr[l...r]之中查找 target
    while (l <= r):
        
