#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for i in range(len(temperatures)):
            startTemp = temperatures[i]
            for j in range(i, len(temperatures)):
                currTemp = temperatures[j]
                count = 0
                if currTemp > startTemp:
                    count = j - i
                    break;
            res.append(count)

        
        return res

Solution().dailyTemperatures([73,74,75,71,69,72,76,73])
                


# @lc code=end

