import math, random, datetime
import arr as randomList

now = datetime.datetime.now()

# 没有重复元素的数组 or 少量重复的数组
def quickSortNoRepeat(sortList) :
    # 基线条件：为空或者只包含一个元素的数组是‘有序’的
    if len(sortList) < 2 :
        return sortList

    # 递归条件
    # 优化快速排序, 对于近似于有序的数组，使用随机快速排序
    # 随机生成基准值，最后和数组的第一个值进行数据交换
    ran = int(math.floor(random.random() * len(sortList)))
    sortList[0], sortList[ran] = sortList[ran], sortList[0]
    pviot = sortList[0]

    # 由所有小于等于基准值的元素组成的子数组
    less = [i for i in sortList[1:] if i <= pviot] # i <= pviot
    # 由所有大于基准值的元素组成的子数组
    greater = [j for j in sortList[1:] if j > pviot]
    return quickSortNoRepeat(less) + [pviot] + quickSortNoRepeat(greater)

quickSortNoRepeat(randomList.generateRandomList(1000, 0, 1000))

now = datetime.datetime.now()

def quickSort(sortList, left, right) :
    # 基线条件：为空或者只包含一个元素的数组是‘有序’的
    if len(sortList) < 2 :
        return sortList
    index = partition(sortList, left, right)

    # 递归条件
    if index + 1 > 0 and index + 1 < right :
        quickSort(sortList, left, index - 1)
        quickSort(sortList, index + 1, right)
    return sortList

def partition (arr, l, r) :
    # 优化快速排序 => 随机化快速排序, 对于近似于有序的数组，使用随机快速排序
    # 随机生成基准值，最后和数组的第一个值进行数据交换
    ran = int(math.floor(random.random() * (r - l) + l))
    arr[l], arr[ran] = arr[ran], arr[l]
    pviot = arr[l]

    i = l + 1
    j = r
    while i <= j :
        while i <= r and arr[i] < pviot :
            i += 1
        while j >= l + 1 and arr[j] > pviot :
            j -= 1
        if i > j : break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    arr[l], arr[j] = arr[j], arr[l]
    return j

newList = randomList.generateRandomList(100000, 0, 10)
# newList = [1, 2, 3, 2, 2, 3, 2, 4]
left = 0
right = len(newList) - 1

print(len(quickSort(newList, left, right)))
# print(quickSort(newList, left, right))
future = datetime.datetime.now()
print(future - now)

# class quick_sort(sort_list):
#     def _partition(self, alist, p, r):
#         i = p-1
#         x = alist[r]
#         for j in range(p, r):
#             if alist[j]<=x:
#                 i += 1
#                 alist[i], alist[j] = alist[j], alist[i]
#         alist[i+1], alist[r] = alist[r], alist[i+1]
#         return i+1
#
#     def _quicksort(self, alist, p, r):
#         if p<r:
#             q = self._partition(alist, p, r)
#             self._quicksort(alist, p, q-1)
#             self._quicksort(alist, q+1, r)
#
#     def __call__(self, sort_list):
#         self._quicksort(sort_list, 0, len(sort_list)-1)
#         return sort_list
