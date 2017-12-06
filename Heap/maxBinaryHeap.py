class MaxHeap :
    def __init__(self) :
        self.heapList = [0]
        self.currentSize = 0

    def shiftUp(self, i) :
        while i // 2 > 0 :
            if self.heapList[i] > self.heapList[i // 2] :
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2

    def insert (self, k) :
        self.heapList.append(k)
        self.currentSize += 1
        self.shiftUp(self.currentSize)

    def shiftDown(self, k) :
        # 该节点一定有一个子节点
        while (2 * k) <= self.currentSize :
            j = 2 * k
            if j + 1 <= self.currentSize and self.heapList[j + 1] > self.heapList[j] :
                j += 1

            if self.heapList[k] >= self.heapList[j] : break
            self.heapList[k], self.heapList[j] = self.heapList[j], self.heapList[k]
            k = j

    def delMax(self) :
        if self.currentSize == 0:
            return print('no elements')
        ret = self.heapList[1]
        self.heapList[1], self.heapList[self.currentSize] = self.heapList[self.currentSize], self.heapList[1]
        self.currentSize -= 1
        self.heapList.pop()
        self.shiftDown(1)
        return ret

    def buildHeap(self, alist) :
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        print(self.heapList)
        while i > 0 :
            self.shiftDown(i)
            i -= 1

bh = MaxHeap()
bh.buildHeap([3, 2, 4, 6, 7, 1, 8, 5])
print(bh.delMax())
print(bh.delMax())
print(bh.delMax())
print(bh.delMax())
print(bh.delMax())
print(bh.delMax())
print(bh.delMax())
print(bh.delMax())
print(bh.heapList, bh.currentSize)
