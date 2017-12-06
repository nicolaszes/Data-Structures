# 假设待排序列都是正整数
# 计数排序在输入 n个 0到 k之间的整数时
# 时间复杂度最好情况下为 O(n+k)
# 最坏情况下为 O(n+k)
# 平均情况为 O(n+k)
# 空间复杂度为 O(n+k)
# 计数排序是稳定的排序

import math, random, datetime
import arr as randomList
now = datetime.datetime.now()

def countSort(lista) :
    c = []
    res = []
    for i in range(0, 100):
        c.append(0)
    print('len', len(c))

    for i in range(0, len(lista)) :
        c[lista[i]] = c[lista[i]] + 1
        res.append(0)
    print('len', len(c))
    print('len', len(res))

    for i in range(0, 100) :
        c[i] = c[i - 1] + c[i]      #c中此时存放的是小于或者等于i的数字的个数

    for i in range(len(lista) - 1, -1, -1) :
        res[c[lista[i]] - 1] = lista[i]
        c[lista[i]] = c[lista[i]] - 1

    return res;

newList = randomList.generateRandomList(100000, 0, 10)
print(len(countSort(newList)))

future = datetime.datetime.now()
# 测试排序速度
print('计数排序', future - now)
