# 假设待排序列都是正整数
# def countSort (arr) :
#     B = []
#     C = []
#     arrMin = arrMax = arr[0]
#
#     for i in range(0, len(arr)) :
#         arrMin = arrMin if arrMin <= arr[i] else arr[i]
#         arrMax = arrMax if arrMax >= arr[i] else arr[i]
#
#         print(i, arr[i])
#         print(C.index(arr[i]))
#         return null
#         C[arr[i]] = C[arr[i]] + 1 if C[arr[i]] else 1
#     print(arrMin, arrMax, C)
#
#     for j in range(arrMin, arrMax) :
#         C[j + 1] = (C[j + 1] or 0) + (C[j] or 0)
#
#     for k in range(len(arr), -1, -1) :
#         B[C[arr[k]] - 1] = arr[k]
#         C[arr[k]] -= 1
#     return B

def countSort (alist, k) :
    print(k)
    print(len(alist))
    alist3 = [0 for i in range(k)]
    alist2 = [0 for i in range(len(alist))]

    print(alist2)
    print(alist3)

    for j in alist :
        alist3[j] += 1
    print(alist3)

    for i in range(1, k) :
        alist3[i] = alist3[i - 1] + alist3[i]

    for l in alist[::-1] :
        alist2[alist3[l] - 1] = l
        alist3[l] -= 1

    return alist2

newArr = [6, 3, 2, 5, 4]
print(countSort(newArr, len(newArr)))
