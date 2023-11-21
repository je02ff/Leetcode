#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        indexMap = {}
        answerList = []
        left = 0 
        right = len(nums) - 1

        while right > left:
            sum = nums[left] + nums[right]
            if  -1*sum in indexMap:
                answerList.append([nums[left], nums[right], nums[-sum]])
        
        return answerList
# @lc code=end

