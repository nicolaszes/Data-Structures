import sys, datetime
sys.path.append("..")
import arr as randomList

now = datetime.datetime.now()

# 求arr[l..r]范围的逆序数对个数
def inversionPair (arr, l, r) :
    if l >= r : return 0

    mid = int(l + (r - l) / 2)

    # 求出 arr[l...mid] 范围的逆序数
    res1 = inversionPair(arr, l , mid)
    # 求出 arr[mid+1...r] 范围的逆序数
    res2 = inversionPair(arr, mid + 1 , r)

    return res1 + res2 + merge(arr, l, mid, r)

# merge 函数求出在 arr[l...mid] 和 arr[mid+1...r] 分别有序的基础上
# arr[l...r]的逆序数对个数
def merge (arr, l, mid, r) :
    # aux = int(r - l + 1);

    aux = arr[l:r + 1]
    # print(aux)
    for index in range(l, r + 1) :
        # print('index', index - l, index)
        aux[index- l] = arr[index]

    res = 0
    j = l
    k = mid + 1

    for i in range(l, r + 1) :
        # print('__________k-l / k-l / i =>', j-l, k-l, i)
        # 如果左半部分元素已经全部处理完毕
        if j > mid :
            arr[i] = aux[k - l]
            k += 1

        # 如果右半部分元素已经全部处理完毕
        elif k > r :
            arr[i] = aux[j - l]
            j += 1

        # 左半部分所指元素 <= 右半部分所指元素
        elif aux[j - l] <= aux[k - l] :
            arr[i] = aux[j - l]
            j += 1

        # 右半部分所指元素 < 左半部分所指元素
        else :
            arr[i] = aux[k - l]
            k += 1

            # 此时, 因为右半部分k所指的元素小
            # 这个元素和左半部分的所有未处理的元素都构成了逆序数对
            # 左半部分此时未处理的元素个数为 mid - j + 1
            # print('___________mid - j + 1',mid - j + 1)
            res += mid - j + 1
    return res

newArr = randomList.generateRandomList(1000000, 0, 1000)
# newArr = [10, 9, 8, 7, 6, 5, 4, 3 , 2, 1]
left = 0
right = len(newArr) - 1
print(inversionPair(newArr, left, right))

future = datetime.datetime.now()
# 测试排序速度
print('逆序对', future - now)
