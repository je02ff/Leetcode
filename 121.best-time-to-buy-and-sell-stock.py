#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyPrice = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > buyPrice:
                maxProfit = max(maxProfit, prices[i] - buyPrice)
            else:
                buyPrice = prices[i]
        return maxProfit


# @lc code=end