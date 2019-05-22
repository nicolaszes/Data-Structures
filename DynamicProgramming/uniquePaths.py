class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [([1] * n) for row in range(m)]
        for i in reversed(range(m - 1)):
            for j in reversed(range(n - 1)):
                matrix[i][j] = matrix[i + 1][j] + matrix[i][j + 1]
        return matrix[0][0]