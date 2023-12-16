#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


# 1. get middle row
# 2. is first element of middle row the number?
# 3. is first element of middle row higher or lower than target?
# 4. if higher than target -> first row is mid row + 1
#    if lower than target -> 
#    else -> bottom row is mid row - 1
# @lc code=end

