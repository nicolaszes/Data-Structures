import sys, datetime
sys.path.append("../Sort")
import arr as randomList

now = datetime.datetime.now()

def heapSort (arr, n) :
    for i in range((n - 1) // 2, -1, -1) :
        shiftDown(arr, n, i)

    for i in range(n - 1, -1, -1) :
        arr[0], arr[i] = arr[i], arr[0]
        shiftDown(arr, i, 0)

    return arr

def shiftDown (arr, n, k) :
    while 2 * k + 1 < n :
        j = 2 * k + 1 # arr[j] 和 arr[k]
        if j + 1 < n and arr[j + 1] > arr[j] :
            j += 1
        if arr[k] >= arr[j] : break
        arr[k], arr[j] = arr[j], arr[k]
        k = j

newArr = randomList.generateRandomList(100000, 0, 10)
# newArr = [10, 9, 8, 7, 6, 5, 4, 3 , 2, 1]
heapSort(newArr, len(newArr))
future = datetime.datetime.now()
print('堆排序', future - now)
