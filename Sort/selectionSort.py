def selectionSort(sortList) :
    if len(sortList) < 2 :
        return sortList
    # 找出数组中最小值，将其放到第一位
    # 找出数组第二小的值，将其放到第二位
    for i in range(len(sortList) - 1) :
        smallest = sortList[i]
        location = i

        for j in range(i, len(sortList)) :

            if sortList[j] < smallest :
                print(i, len(sortList))
                print(j)
                smallest = sortList[j]
                location = j

        # 如果当前值不小于前一个值，位置交换
        if i != location :
            sortList[i], sortList[location] = sortList[location], sortList[i]
    return sortList

print(selectionSort([2, 4, 6, 5, 1, 3]))
