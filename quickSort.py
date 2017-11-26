def quickSort(array) :
    # 基线条件：为空或者只包含一个元素的数组是‘有序’的
    if len(array) < 2 :
        return array
    
    else :
        # 递归条件
        pviot = array[0]
        # 由所有小于等于基准值的元素组成的子数组
        less = [i for i in array[1:] if i < pviot]
        # 由所有大于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i > pviot]
        return quickSort(less) + [pviot] + quickSort(greater)
print(quickSort([1, 3, 6, 4, 2]))
