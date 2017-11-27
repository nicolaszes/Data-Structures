def insertSort (sortList) :
    # 基线条件：为空或者只包含一个元素的数组是‘有序’的
    if len(sortList) < 2 :
        return sortList
    for i in range(1, len(sortList)) :
        # 当 list的前一个数字大于后一个数字，进行位置调换
        # i - 1，循环判断前一个数是否大于后一个数
        while i >= 1 and sortList[i - 1] > sortList[i] :
            sortList[i], sortList[i - 1] = sortList[i - 1], sortList[i]
            i -= 1
    return sortList

print(insertSort([3, 2, 5, 4, 6, 1]))
