class Solution:
    def totalNQueens(self, n: int):
        if n < 1: return []
        self.count = 0
        self.DFS(self, 0, 0, 0, 0)
        return self.count
    
    def DFS(self, n, row, col, xy_dif, xy_sum):
        # 递归终止条件
        if row >= n:
            self.count += 1
            return
        # 得到当前所有空位
        bits = (~(col | xy_dif | xy_sum)) & ((1 << n) - 1)

        while bits:
            # 取最低位的 1
            p = bits & -bits
            self.DFS(n, row + 1, col | p, (xy_dif | p) << 1, (xy_sum | p) >> 1)
            # 去掉最低位的 1
            bits= bits & (bits - 1)