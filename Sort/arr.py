import math, random, datetime

# 随机数组生成之前
before = datetime.datetime.now()

def generateRandomList (n, rangeL, rangeR) :
    if rangeL > rangeR :
        return print('rangeL should smaller than rangeR')
    i = 0
    randomList = []
    while i < n:
        # 生成随机数
        ranNum = math.floor(random.random() * (rangeR - rangeL + 1)) + rangeL
        randomList.append(ranNum)
        i += 1
    return randomList

# 随机数组生成之后
now = datetime.datetime.now()
# 随机数组生成耗时
print(now - before)
