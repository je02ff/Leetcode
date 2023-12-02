#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answerList = []
        nums.sort()
        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]:
                continue
            left = index + 1
            right = len(nums) - 1
            while (right > left):
                if nums[index] + nums[left] + nums[right] == 0:
                    answerList.append([nums[index], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif nums[index] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1

        return answerList
Solution().threeSum([-1,0,1,2,-1,-4])
# @lc code=end

