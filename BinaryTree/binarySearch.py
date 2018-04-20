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

    if mid == 0 and target != arr[mid]:
        return -1
        
    if target < arr[mid]:
        return recursionBinarySearch(arr[0:mid], left, target)
    elif target > arr[mid]:
        left = left + mid
        return recursionBinarySearch(arr[mid:len(arr)+1], left, target)
    else:
        return left + mid

array = [-1,0,1,2,3,4,5,6,7,8,10,13,14,16,18,19,40]
print(recursionBinarySearch(array, 0, 2))
        