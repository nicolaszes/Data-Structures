import datetime
import arr as randomList

now = datetime.datetime.now()

def bubbleSort (sortList) :
    # 基线条件：为空或者只包含一个元素的数组是‘有序’的
    if (len(sortList) < 2) :
        return sortList

    # 遍历 0,0-3，1,0-2，2,0-1
    for i in range(len(sortList) - 1) :
        for j in range(len(sortList) - i - 1) :
            if sortList[j] > sortList[j + 1] :
                sortList[j], sortList[j + 1] = sortList[j + 1], sortList[j]
    return sortList

bubbleSort(randomList.generateRandomList(10000, 0, 10))

future = datetime.datetime.now()
print(future - now)
