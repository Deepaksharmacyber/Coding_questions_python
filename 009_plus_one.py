"""
------------------------------------------------------------
LeetCode Problem: 66. Plus One
Link: https://leetcode.com/problems/plus-one/description/?envType=problem-list-v2&envId=v6gm6bgd
------------------------------------------------------------

You are given an array of digits representing a non-negative
integer. The array does not contain leading zeros.

Increment the integer by one and return the resulting array
of digits.

Example:
Input:  [1,2,3]
Output: [1,2,4]

------------------------------------------------------------
Time Complexity:  O(n)
Space Complexity: O(1)

Explanation:
We traverse the array from right to left. If adding 1 causes
a carry (digit becomes 10), we set it to 0 and continue.
Otherwise, we increment and return immediately.

If all digits are 9 (e.g., [9,9,9]), we insert 1 at the
front to form numbers like [1,0,0,0].
------------------------------------------------------------
"""

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # Traverse digits from right to left
        for i in range(len(digits) - 1, -1, -1):
            
            # If no carry is generated
            if digits[i] + 1 <= 9:
                digits[i] += 1
                return digits   # End early
            
            # Carry generated → set current digit to 0
            digits[i] = 0
        
        # If all digits were 9 → add 1 at front
        digits.insert(0, 1)
        return digits


# Example usage (optional for testing):
# sol = Solution()
# print(sol.plusOne([9,9,9]))  # Output: [1,0,0,0]
