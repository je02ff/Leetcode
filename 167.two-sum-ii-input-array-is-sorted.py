#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            answer = []
            for index, num in enumerate(numbers):
                 
            return answer
    
    def search(numbers: List[int]) -> bool:
        l = 0
        r = len(numbers) - 1
        m = (r + 1)// 2

        if numbers[m] == target:
            return m
        
        if numbers[m] > target:
            self.search(numbers[::m], target)
        else:
            self.search(numbers[l::], target)


Solution().twoSum([2,7,11,15], 9)
# @lc code=end

