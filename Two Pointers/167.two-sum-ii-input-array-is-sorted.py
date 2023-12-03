#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while right > left:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1] 

            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1



print(Solution().twoSum([2,7,11,15], 9))
# @lc code=end

