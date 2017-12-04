# 假设待排序列都是正整数
import math, random, datetime
import arr as randomList
now = datetime.datetime.now()

def countSort(lista):
    c = []
    res = []
    for i in range(0, 100):
        c.append(0)

    for i in range(0,len(lista)) :
        c[lista[i]] = c[lista[i]] + 1
        res.append(0)

    for i in range(0,100):
        c[i] = c[i - 1] + c[i]      #c中此时存放的是小于或者等于i的数字的个数

    for i in range(len(lista) - 1, -1, -1):
        res[c[lista[i]] - 1] = lista[i]
        c[lista[i]] = c[lista[i]] - 1

    return res;

newList = randomList.generateRandomList(100000, 0, 10)
print(len(countSort(newList)))

future = datetime.datetime.now()
# 测试排序速度
print('计数排序', future - now)
