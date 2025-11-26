"""
LeetCode Problem: 13. Roman to Integer
Link: https://leetcode.com/problems/roman-to-integer/

Description:
Roman numerals are represented by seven symbols: I, V, X, L, C, D, and M.
Given a roman numeral, convert it to an integer.

Rules:
- If a smaller value appears before a larger value, subtract the smaller.
- Otherwise, add all values normally.

Examples:
- III -> 3
- LVIII -> 58 (L = 50, V = 5, III = 3)
- MCMXCIV -> 1994

Constraints:
- 1 <= s.length <= 15
- s contains only 'I', 'V', 'X', 'L', 'C', 'D', 'M'
- Input is always valid (1 to 3999)

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        # Mapping of Roman symbols to values
        vals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        total = 0
        n = len(s)
        
        for i in range(n):
            cur = vals[s[i]]
            # Look ahead to next symbol; if none exists, treat as 0
            nxt = vals[s[i+1]] if i + 1 < n else 0
            
            # Subtract if current < next (subtractive pair)
            if cur < nxt:
                total -= cur
            else:
                total += cur
        
        return total
