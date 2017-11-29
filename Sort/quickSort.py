import math
import random
def quickSort(sortList) :
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
    less = [i for i in sortList[1:] if i < pviot]
    # 由所有大于基准值的元素组成的子数组
    greater = [j for j in sortList[1:] if j > pviot]
    return quickSort(less) + [pviot] + quickSort(greater)
print(quickSort([1, 3, 6, 4, 2, 5]))
