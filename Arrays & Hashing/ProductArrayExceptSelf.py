'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        post = []
        
        product = 1
        for num in nums:
            product *= num
            pre.append(product)

        product = 1
        for num in reversed(nums):
            product *= num
            post.append(product)
        post.reverse()
        answer = []
        for i in range(len(nums)):
            if i-1 in range(len(nums)):
                preProduct = pre[i-1]
            else:
                 preProduct = 1
            if i+1 in range(len(nums)):
                postProduct = post[i+1]
            else:
                 postProduct = 1
            answer.append(preProduct*postProduct)
        
        return answer
            
print(Solution().productExceptSelf([1,2,3,4]))
                