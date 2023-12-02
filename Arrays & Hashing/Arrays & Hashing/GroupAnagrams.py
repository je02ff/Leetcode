'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
'''

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for string in strs:
            sortedString = ''.join(sorted(string))
            if sortedString in group:
                group[sortedString].append(string)
            else:
                group[sortedString] = [string]
        return [values for values in group.values()]
         

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))