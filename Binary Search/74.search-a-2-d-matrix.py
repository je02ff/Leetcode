#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        topRow = 0
        bottomRow = len(matrix) - 1

        while bottomRow >= topRow:
            midRow = ((bottomRow - topRow) // 2) + topRow

            if matrix[midRow][0] == target or matrix[midRow][-1] == target:
                return True
            
            if matrix[midRow][0] < target < matrix[midRow][-1]:
                left = 0
                right = len(matrix[midRow]) - 1

                while right >= left:
                    mid = ((right - left) // 2) + left

                    if target == matrix[midRow][mid]:
                        return True
                    
                    if target > matrix[midRow][mid]:
                        left = mid + 1

                    if target < matrix[midRow][mid]:
                        right = mid - 1

            if target > matrix[midRow][0]:
                topRow = midRow + 1
            if target < matrix[midRow][0]:
                bottomRow = midRow - 1

        return False

Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
# 1. get middle row
# 2. is first element of middle row the number?
# 3. is first element of middle row higher or lower than target?
# 4. if higher than target -> first row is mid row + 1
#    if lower than target -> 
#    else -> bottom row is mid row - 1
# @lc code=end

