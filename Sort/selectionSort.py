import datetime
import arr as randomList

now = datetime.datetime.now()

def selectionSort(sortList) :
    if len(sortList) < 2 :
        return sortList
    # 找出数组中最小值，将其放到第一位
    # 找出数组第二小的值，将其放到第二位
    for i in range(len(sortList) - 1) :
        smallest = sortList[i]
        location = i

        for j in range(i, len(sortList)) :

            if sortList[j] < smallest :
                # print(i, len(sortList))
                # print(j)
                smallest = sortList[j]
                location = j

        # 如果当前值不小于前一个值，位置交换
        if i != location :
            sortList[i], sortList[location] = sortList[location], sortList[i]
    return sortList

selectionSort(randomList.generateRandomList(10000, 0, 10))

future = datetime.datetime.now()
print(future - now)


# 存储最小元素的值
# 存储最小元素的索引
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# 对数组进行排序
def selectSort(arr):
    newArr = []
    for j in range(len(arr)):
        # 找出数组中最小的元素，并将其加入到新的数组中
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

# print(selectSort([5, 3, 6, 2, 10]))
