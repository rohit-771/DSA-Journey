class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        ans = []

        def isSafe(row, col):
            i = row - 1
            while i >= 0:
                if board[i][col] == 'Q':
                    return False
                i -= 1

            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def fun(row):
            if row == n:
                ans.append([''.join(r) for r in board])
                return

            for col in range(n):
                if isSafe(row, col):
                    board[row][col] = 'Q'
                    fun(row + 1)
                    board[row][col] = '.'

        fun(0)
        return ans
            