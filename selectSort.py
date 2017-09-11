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

print(selectSort([5, 3, 6, 2, 10]))
