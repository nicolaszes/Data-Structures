class Solution:
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     if board is None or len(board) == 0:
    #         return False
    #     return self.solve(board)

    # def solve(self, board):
    #     for i in range(len(board)):
    #         for j in range(len(board[0])):
    #             if (board[i][j] == '.'):
    #                 for c in range(1, 10):
    #                     if self.isValid(board, i, j, str(c)):
    #                         print(board, i, j, str(c))
    #                         board[i][j] = str(c)
    #                         if self.solve(board):
    #                             return True
    #                         else:
    #                             board[i][j] = '.'
    #                 return False
    #     return True
    
    # def isValid(self, board, row, col, c):
    #     for i in range(9):
    #         if board[i][col] != '.' and board[i][col] == c:
    #             return False
    #         if board[row][i] != '.' and board[row][i] == c:
    #             return False
    #         if board[3 * int(row / 3) + int(i / 3)][3 * int(col / 3) + int(i % 3)] != '.' and board[3 * int(row / 3) + int(i / 3)][3 * int(col / 3) + int(i % 3)] == c:
    #             return False
    #     return True

    def isValidSudoku(self, board):
        '''
        :type board: List[List[str]]
        :rtype: bool
        '''
        rows = [{} for i in range(9)] #记录行出现过的数字
        cols = [{} for i in range(9)] #记录列出现过的数字
        subs = [[{} for i in range(3)] for j in range(3)] #记录小方块出现过的数字
        
        for i in range(9):
            for j in range(9):
                d = board[i][j]
                if d == '.':
                    continue
                if (d in rows[i]) or (d in cols[j]) or (d in subs[int(i/3)][int(j/3)]):
                    return False
                rows[i][d] = 1
                cols[j][d] = 1
                subs[int(i/3)][int(j/3)][d] = 1
        
        return True
