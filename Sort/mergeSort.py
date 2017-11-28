import math

# 分而治之的思想
def mergeSort (sortList) :
    if len(sortList) == 1 :
        return sortList

    mid = int(math.floor(len(sortList) / 2))
    left = sortList[0:mid]
    right = sortList[mid:]

    # 递归调用 mergeSort方法
    return merge(mergeSort(left), mergeSort(right))

def merge (left, right) :
    # print(16, left)
    # print(17, right)
    # 以空间换时间，新建了一个 result的变量
    result = []
    il = 0
    ir = 0

    while il < len(left) and ir < len(right) :
        if left[il] < right[ir] :
            result.append(left[il])
            il += 1
        else :
            result.append(right[ir])
            ir += 1

    while il < len(left) :
        result.append(left[il])
        il += 1

    while ir < len(right) :
        result.append(right[ir])
        ir += 1

    return result

print(mergeSort([3, 2, 6, 5, 4, 7, 1]))
