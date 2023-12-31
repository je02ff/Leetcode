#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxVolume = 0
        while right > left:
            tempVolume = min(height[left], height[right]) * (right - left)
            if tempVolume > maxVolume:
                maxVolume = tempVolume
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxVolume
            

            
# @lc code=end

