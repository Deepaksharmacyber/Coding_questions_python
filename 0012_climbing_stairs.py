"""
LeetCode Problem: Climbing Stairs
Link: https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.
Each time you can take either 1 step or 2 steps.
Return the number of distinct ways to climb to the top.

Example:
Input: n = 3
Output: 3

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2

        prev2 = 1  # ways to reach step 1
        prev1 = 2  # ways to reach step 2

        # For each step, ways = sum of previous two steps (Fibonacci pattern)
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1


# Uncomment below lines to test locally
# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.climbStairs(3))  # Output: 3
#     print(sol.climbStairs(5))  # Output: 8
