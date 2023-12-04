#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while right >= left:
            mid = ((right - left) // 2) + left
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                right = mid - 1

            if nums[mid] < target:
                left = mid + 1



        return -1


Solution().search([5], 5)

# @lc code=end

