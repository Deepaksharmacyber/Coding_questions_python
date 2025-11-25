"""
LeetCode Problem: 9. Palindrome Number
Link: https://leetcode.com/problems/palindrome-number/

Description:
Given an integer x, return True if x is a palindrome, and False otherwise.

An integer is a palindrome when it reads the same forward and backward.
For example:
- 121 is a palindrome
- 123 is not a palindrome

Constraints:
- -2^31 <= x <= 2^31 - 1
- Negative numbers are NOT palindromes
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are NOT palindromes
        if x < 0:
            return False
        
        original = x
        reverse = 0
        
        # Famous 3-line palindrome logic
        while x > 0:
            last_digit = x % 10
            reverse = reverse * 10 + last_digit
            x = x // 10
        
        return reverse == original
