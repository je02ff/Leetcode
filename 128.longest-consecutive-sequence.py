#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNumbers = set(nums)

        maxSequence = 0
        for num in nums:
            count = 0
            if num - 1 in uniqueNumbers:
                continue
            else:
                count = 1
                while (num + 1 in uniqueNumbers):
                    count += 1
                    num += 1
                if count > maxSequence:
                    maxSequence = count
        
        return maxSequence
            
Solution().longestConsecutive([100,4,200,1,3,2])
# @lc code=end

