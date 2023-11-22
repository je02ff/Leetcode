#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVolume = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                smallestHeight = min(height[i], height[j])
                tempArea = smallestHeight * (j - i)

                if maxVolume <  tempArea:
                    maxVolume = tempArea
        return maxVolume
            

            
# @lc code=end

