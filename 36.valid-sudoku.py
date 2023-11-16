#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = [[set() for _ in range(3)] for _ in range(3)]
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]

        for col in range(9):
            for row in range(9):
                if board[row][col] == '.':
                    continue

                if board[row][col] not in rows[row]:
                    (rows[row]).add(board[row][col])
                else:
                    return False

                if board[row][col] not in columns[col]:
                    columns[col].add(board[row][col])
                else:
                    return False

                if board[row][col] not in squares[row // 3][ col // 3]:
                    (squares[row // 3][ col // 3]).add(board[row][col])
                else:
                    return False
        return True

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

Solution().isValidSudoku(board)
# @lc code=end

