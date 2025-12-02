"""
LeetCode Problem: Search Insert Position
Link: https://leetcode.com/problems/search-insert-position/

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def searchInsert(self, nums, target):
        # Binary Search Approach
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Case 1: target found
            if nums[mid] == target:
                return mid
            
            # Case 2: target is in the right half
            elif nums[mid] < target:
                left = mid + 1
            
            # Case 3: target is in the left half
            else:
                right = mid - 1
        
        # If not found, left is the correct insert position
        return left
