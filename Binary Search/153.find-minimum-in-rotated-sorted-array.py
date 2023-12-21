#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        if right == 0:
            return nums[0]
        
        while (right - left) != 1:
            mid = ((right - left) // 2) + left

            if nums[left] < nums[mid] < nums[right]:
                return nums[left]
            
            if nums[left] > nums[right] > nums[mid]:
                if nums[mid - 1] > nums[mid] < nums[mid + 1]:
                    return nums[mid]
                else:
                    right = mid 
            if nums[mid] > nums[left] > nums [right]:
                left = mid
        if nums[left] < nums[right]:
            return nums[left]
        else:
            return nums[right]
Solution().findMin([3,4,5,1,2])
# @lc code=end

