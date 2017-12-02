import sys, math, random, datetime
sys.path.append("..")
import arr as randomList
# import quickSort as qSort

# 双路快排和三路快排的思想能不能用在selection算法中? :)
# 求出arr[l...r]范围里第k小的数
def __selection (arr, n, k) :
    if k >= 0 and n < k : return 0

    return selection(arr, 0, n, k)

def selection (arr, l, r, k) :
    if l == r : return arr[l]

    # partition之后, arr[p]的正确位置就在索引p上
    p = partition(arr, l, r)
    # 如果 k == p, 直接返回arr[p]
    if k == p : return arr[p]
    # 如果 k < p, 只需要在arr[l...p-1]中找第k小元素即可
    elif k < p : return  selection(arr, l, p - 1, k)
    # 如果 k > p, 则需要在arr[p+1...r]中找第k小元素
    else : return selection(arr, p + 1, r, k)

def partition (arr, l, r) :
    ran = int(math.floor(random.random() * (r - l + 1) + l))
    arr[l], arr[ran] = arr[ran], arr[l]

    # [l+1...j] < p ; [lt+1..i) > p
    j = l
    # print(l + 1, r + 1)
    # for i in range(l + 1)
    for i in range(l + 1, r + 1) :
        if arr[i] < arr[l] :
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j


newArr = randomList.generateRandomList(10000, 0, 100)
# newArr = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(newArr) - 1
# 求出arr[l...r]范围里第k小的数
print(__selection(newArr, n, 8888))
# qSort.quickSortInThreeWays(newArr, 0, n)
