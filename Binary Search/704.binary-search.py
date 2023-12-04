#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def scan(left: int, right: int, nums: List[int], target: int):
            mid = ((right - left) // 2) + left
            
            if right < left:
                return -1

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                return scan(left,mid - 1,nums, target)
            else:
                return scan(mid + 1,right,nums, target)
        
        left = 0
        right = len(nums) - 1

        return scan(left, right, nums, target)


Solution().search([-1,0,3,5,9,12], 2)

# @lc code=end

