"""
LeetCode Problem: 14. Longest Common Prefix
Link: https://leetcode.com/problems/longest-common-prefix/

Description:
Write a function to find the longest common prefix string among an array of strings.
If there is no common prefix, return an empty string "".

Examples:
1. Input: ["flower","flow","flight"]
   Output: "fl"

2. Input: ["dog","racecar","car"]
   Output: ""
   Explanation: There is no common prefix among the input strings.

Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] contains only lowercase English letters (if non-empty)

Approach:
Use prefix shrinking. Start by assuming the first string is the prefix.
For each subsequent string, compare letters one-by-one and reduce the prefix
until they match. Prefix always stays the same or becomes shorter.

Time Complexity: O(n * m), where n = number of strings, m = length of shortest string
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Start with the first string as prefix
        prefix = strs[0]

        # Compare prefix against each string
        for i in range(1, len(strs)):
            cur = strs[i]
            inner_prefix = ""

            # Compare characters of prefix and current string
            length = min(len(prefix), len(cur))

            for j in range(length):
                if prefix[j] == cur[j]:
                    inner_prefix += prefix[j]
                else:
                    break

            prefix = inner_prefix  # shrink prefix
            
            if prefix == "":
                return ""

        return prefix
