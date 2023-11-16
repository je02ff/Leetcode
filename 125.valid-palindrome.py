#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strip = (''.join(char for char in s if char.isalnum())).lower()

        if strip == '':
            return True
        
        start = 0
        end = len(strip) -1

        while start < end:
            if strip[start] != strip[end]:
                return False
            start += 1
            end -= 1
    
        return True

# @lc code=end

