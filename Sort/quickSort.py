import math, random, datetime
import arr as randomList
# import insertSort as insert

now = datetime.datetime.now()

'''
基础快速排序
没有重复元素的数组 or 少量重复的数组
'''
def quickSortNoRepeat(sortList) :
    # 基线条件：为空或者只包含一个元素的数组是‘有序’的
    if len(sortList) < 2 : return sortList

    '''
    递归条件
    优化快速排序, 对于近似于有序的数组，使用随机快速排序
    随机生成基准值，最后和数组的第一个值进行数据交换
    '''
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

'''
双路快速排序
存在大量的重复元素的数组
'''
def quickSortInTwoWays(sortList, left, right) :
    # 基线条件：为空或者只包含一个元素的数组是‘有序’的
    if right - left < 2 :
        return sortList
    index = partitionInTwoWays(sortList, left, right)

    # 递归条件
    # if index > 1 and index < right - 1 :
    quickSortInTwoWays(sortList, left, index - 1)
    quickSortInTwoWays(sortList, index + 1, right)
    return sortList

def partitionInTwoWays (arr, l, r) :
    # 优化快速排序 => 随机化快速排序, 对于近似于有序的数组，使用随机快速排序
    # 随机生成基准值，最后和数组的第一个值进行数据交换
    ran = int(math.floor(random.random() * (r + l) / 2))
    arr[l], arr[ran] = arr[ran], arr[l]
    pviot = arr[l]

    # arr[l + 1, i) <= pviot; arr(j, r] >= pviot
    i = l
    j = r
    # (i, j)这个区间
    while i <= j :
        while arr[i] < pviot :
            i += 1
        while arr[j] > pviot :
            j -= 1
        if i > j : break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    arr[l], arr[j] = arr[j], arr[l]
    return i

newList = randomList.generateRandomList(300, 0, 10)
left = 0
right = len(newList) - 1

print(quickSortInTwoWays(newList, left, right))
# print(len(quickSortInTwoWays(newList, left, right)))
future = datetime.datetime.now()
# 测试排序速度
print('双路快速排序', future - now)

'''
 三路快速排序
 面向对象封装
'''
lis = [1, 2, 3]
def quickSortInThreeWays (arr, l, r) :
    # 基线条件：为空或者只包含一个元素的数组是‘有序’的
    if r - l < 2 :
        return arr

    # partition
    ran = int(math.floor(random.random() * (r - l) + l))
    arr[l], arr[ran] = arr[ran], arr[l]
    pviot = arr[l]

    lt = l # arr[l + 1...lt]
    gt = r + 1 # arr[gt...r]
    i = l + 1 # arr[lt + 1...i)

    while i < gt :
        if arr[i] < pviot :
            arr[i], arr[lt + 1] = arr[lt + 1], arr[i]
            lt += 1
            i += 1
        elif arr[i] > pviot :
            arr[i], arr[gt - 1] = arr[gt - 1], arr[i]
            gt -= 1
        else :
            i += 1
    arr[l], arr[lt] = arr[lt], arr[l]

    # 递归条件
    quickSortInThreeWays(arr, l, lt - 1)
    quickSortInThreeWays(arr, gt, r)
    return arr

newList = randomList.generateRandomList(300, 0, 10)
left = 0
right = len(newList) - 1
print(quickSortInThreeWays(newList, left, right))
print(len(quickSortInThreeWays(newList, left, right)))

ai = datetime.datetime.now()
# 测试排序速度
print('三路快速排序', ai - future)

'''
 双路快速排序
 面向对象封装
'''
class quick_sort():
    def _partition(self, alist, p, r):
        i = p - 1
        x = alist[r]
        for j in range(p, r):
            if alist[j] <= x:
                i += 1
                alist[i], alist[j] = alist[j], alist[i]
        alist[i + 1], alist[r] = alist[r], alist[i+1]
        return i + 1

    def _quicksort(self, alist, p, r):
        if p<r:
            q = self._partition(alist, p, r)
            self._quicksort(alist, p, q - 1)
            self._quicksort(alist, q + 1, r)

    def __call__(self, sort_list):
        self._quicksort(sort_list, 0, len(sort_list) - 1)
        return sort_list

print(quick_sort)
