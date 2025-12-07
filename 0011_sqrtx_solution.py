# ------------------------------------------------------------
# LeetCode Problem: 69. Sqrt(x)
# Difficulty: Easy
# ------------------------------------------------------------
# Given a non-negative integer x, return the square root of x 
# rounded down to the nearest integer. The returned integer 
# must not be negative.
#
# You must NOT use any built-in exponent function such as:
#   pow(x, 0.5)
#   x ** 0.5
#
# Examples:
# Input: 4  -> Output: 2
# Input: 8  -> Output: 2 (because sqrt(8) ≈ 2.82, floor is 2)
#
# ------------------------------------------------------------
# TIME & SPACE COMPLEXITY:
# Time Complexity:  O(log x)
#    - Binary search repeatedly halves the search space.
#
# Space Complexity: O(1)
#    - No extra data structures used; only variables.
# ------------------------------------------------------------

class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Returns the integer square root of x using binary search.
        """
        if x < 2:
            return x
        
        left, right = 1, x // 2
        
        while left <= right:
            mid = left + (right - left) // 2
            sq = mid * mid
            
            if sq == x:
                return mid
            elif sq < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right


# ------------------------------------------------------------
# Example Test Cases
# ------------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    
    print("Input: 4  → Output:", sol.mySqrt(4))   # Expected: 2
    print("Input: 8  → Output:", sol.mySqrt(8))   # Expected: 2
    print("Input: 0  → Output:", sol.mySqrt(0))   # Expected: 0
    print("Input: 1  → Output:", sol.mySqrt(1))   # Expected: 1
    print("Input: 25 → Output:", sol.mySqrt(25))  # Expected: 5
