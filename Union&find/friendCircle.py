#   A B C D
# A 1 0 0 1
# B 0 1 1 0
# C 0 1 1 1
# D 1 0 1 1

class UnionFind (object):
    def __init__(self, grid):
        m = len(grid)
        self.count = 0
        self.parent = [0] * m

        for i in range(m):
            self.parent[i] = i
            self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return
        self.parent[rootx] = rooty
        self.count -= 1

class Solution(object):
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M or not M[0]:
            return 0

        uf = UnionFind(M)
        m = len(M)

        # 只需要看矩阵的一半
        for i in range(m):
            for j in range(i + 1, m):
                if M[i][j] == 1:
                    uf.union(i, j)
        return uf.count