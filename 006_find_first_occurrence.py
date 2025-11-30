"""
LeetCode Problem 28: Find the Index of the First Occurrence in a String
-----------------------------------------------------------------------

🔗 Problem Link:
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

📘 Description:
Given two strings `needle` and `haystack`, return the index of the first 
occurrence of `needle` in `haystack`. If `needle` is not part of `haystack`,
return -1.

Your custom approach implemented using sliding window substring matching.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Returns the first index where `needle` occurs in `haystack`.
        Returns -1 if no such index exists.
        """

        # Edge case: if needle is empty, return 0 (LeetCode requirement)
        if needle == "":
            return 0
        
        length_h = len(haystack)
        length_n = len(needle)
        
        # Try each possible index i in haystack
        for i in range(length_h):
            
            # Stop if remaining characters are fewer than needle length
            if i + length_n > length_h:
                break
            
            # Extract substring from haystack of length `length_n`
            text = haystack[i : i + length_n]
            
            # Check if this substring matches needle
            if text == needle:
                return i   # Return the first matching index
        
        # No match found
        return -1



# ----------------------------------------------------------
# Optional: Run a simple manual test when executing this file
# ----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("abcabcabcd", "abcabcd"))   # Expected output: 3
    print(sol.strStr("sadbutsad", "sad"))        # Expected output: 0
    print(sol.strStr("leetcode", "leeto"))       # Expected output: -1
