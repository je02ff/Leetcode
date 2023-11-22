#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = []
        unitsOfRain = 0

        max = 0
        for i in range(len(height)):
            maxLeft += [max]
            if height[i] > max:
                max = height[i]

        max = 0
        for i in range(len(height) -1, -1, -1):
            maxRight = [max] + maxRight
            if height[i] > max:
                max = height[i]

        for i in range(len(height)):
            if min(maxLeft[i], maxRight[i]) - height[i] > 0:
                unitsOfRain += min(maxLeft[i], maxRight[i]) - height[i]

        return unitsOfRain


# @lc code=end

