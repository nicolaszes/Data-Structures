'''
    二分查找法
    binary search
    logN
'''
# 有序数组 arr查找 target
# 如果找到 target，返回相应的索引 index
# 如果找不到 target，返回 -1
def binarySearch (arr, n, target) :
    l = 0
    r = n - 1
    # 在 arr[l...r]之中查找 target
    while (l <= r):
        mid = int(l + (r - l) / 2)
        # print(mid)
        if arr[mid] == target:
            return mid
        
        if target < arr[mid]:
            # 在 arr[l...mid-1]中查找 target
            r = mid - 1
        else:
            # 在 arr[mid+1...r]中查找 target
            l = mid + 1
    return -1
        
array = [-1,0,1,2,3,4,5,6,7,8,10,13,14,16,18,19,40]
print(binarySearch(array, len(array), 40))

def recursionBinarySearch(arr, left, target):
    mid = int(len(arr) / 2)
    # print('mid', mid)

    # 判断 target 不存在 arr 中
    if mid == 0 and target != arr[mid]:
        return -1
        
    if target < arr[mid]:
        # 递归在 arr[0...mid]范围中查找
        return recursionBinarySearch(arr[0:mid], left, target)
    elif target > arr[mid]:
        # 更新索引值
        left = left + mid
        # 递归在 arr[mid...len(arr)+1]范围中查找
        return recursionBinarySearch(arr[mid:len(arr)+1], left, target)
    else:
        return left + mid

array = [-1,0,1,2,3,4,5,6,7,8,10,13,14,16,18,19,40]
print(recursionBinarySearch(array, 0, 2))
        