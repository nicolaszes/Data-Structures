import sys, math, random, datetime
sys.path.append("..")
import arr as randomList
import quickSort as qSort


def __selection (arr, n, k) :
    if k >= 0 and n < k : return 0

    return selection(arr, 0, n, k)

def selection (arr, l, r, k) :
    if l == r : return arr[l]

    p = partition(arr, l, r)
    if k == p : return arr[p]
    elif k < p : return  selection(arr, l, p - 1, k)
    else : return selection(arr, p + 1, r, k)

def partition (arr, l, r) :
    ran = int(math.floor(random.random() * (r - l + 1) + l))
    arr[l], arr[ran] = arr[ran], arr[l]

    # [l+1...j] < p ; [lt+1..i) > p
    j = l
    # print(l + 1, r + 1)
    for i in range(l + 1, r + 1) :
        # print(i)
        if arr[i] < arr[l] :
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j

newArr = randomList.generateRandomList(10000, 0, 100)
# newArr = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(newArr) - 1
print(__selection(newArr, n, 8888))
print(qSort.quickSortInThreeWays(newArr, 0, n))
