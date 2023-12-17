#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
import math
import sys
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        optimalBananaEating = max(piles)
        left, right = 1, optimalBananaEating

        while right >= left:
            eatingSpeed = (right + left) // 2

            eatingHours = 0
            for bananas in piles:
                eatingHours += math.ceil(bananas / eatingSpeed)
            
            if eatingHours <= h:
                optimalBananaEating = min(eatingSpeed, optimalBananaEating)
                right = eatingSpeed - 1
            else:
                left = eatingSpeed + 1

        return optimalBananaEating
    
Solution().minEatingSpeed([3,6,7,11], 8)
# @lc code=end