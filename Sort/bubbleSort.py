def bubbleSort (array) :
    # 基线条件：为空或者只包含一个元素的数组是‘有序’的
    if (len(array) < 2) :
        return array

    # 遍历 0,0-3，1,0-2，2,0-1
    for i in range(len(array) - 1) :
        for j in range(len(array) - i - 1) :
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

print(bubbleSort([4, 2, 3, 6, 1]))
