"""
------------------------------------------------------------
LeetCode Problem: 67. Add Binary
Link: https://leetcode.com/problems/add-binary/?envType=problem-list-v2&envId=v6gm6bgd
------------------------------------------------------------

Given two binary strings a and b, return their sum as a 
binary string.

We add from right to left (like normal addition), keeping
track of the carry, and build the result in reverse order.

------------------------------------------------------------
Time Complexity:  O(n)
Space Complexity: O(n)

Explanation:
We traverse both strings from right to left, adding 
corresponding bits and a carry. Each position is processed 
exactly once → O(n). The result list takes O(n) space.
------------------------------------------------------------
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        # Process bits from right to left
        while i >= 0 or j >= 0 or carry:
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0

            total = bit_a + bit_b + carry

            # Append resulting bit (0 or 1)
            result.append(str(total % 2))

            # Carry will be 0 or 1
            carry = total // 2

            i -= 1
            j -= 1

        # Reverse the result since we built it backward
        return "".join(result[::-1])


# Optional test:
# sol = Solution()
# print(sol.addBinary("1010", "1011"))  # Output: "10101"
