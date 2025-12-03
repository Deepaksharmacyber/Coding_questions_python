"""
------------------------------------------------------------
LeetCode Problem: 58. Length of Last Word
Link: https://leetcode.com/problems/length-of-last-word/description/?envType=problem-list-v2&envId=v6gm6bgd
------------------------------------------------------------

Given a string s consisting of words and spaces, return the
length of the last word in the string.

A word is defined as a maximal substring consisting of 
non-space characters only.

Example:
Input:  "Hello World"
Output: 5

------------------------------------------------------------
Time Complexity:  O(n)
Space Complexity: O(1)

Explanation:
We traverse the string from the end to skip trailing spaces
and then count characters until the previous space or start 
of the string. This requires only one pass → O(n).
------------------------------------------------------------
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        
        # Traverse from end to beginning
        for i in range(len(s) - 1, -1, -1):
            
            # Skip trailing spaces
            if s[i] == ' ' and count == 0:
                continue
            
            # Count letters of the last word
            elif ('a' <= s[i] <= 'z') or ('A' <= s[i] <= 'Z'):
                count += 1
            
            # If a space is found after counting → stop
            else:
                break
        
        return count


# Example usage (optional):
# sol = Solution()
# print(sol.lengthOfLastWord("Hello World"))  # Output: 5
