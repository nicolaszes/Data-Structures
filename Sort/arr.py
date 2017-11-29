import math, random, datetime
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

now = datetime.datetime.now()
print(now - before)
