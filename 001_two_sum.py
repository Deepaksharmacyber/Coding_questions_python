"""
LeetCode Problem: 1. Two Sum
Link: https://leetcode.com/problems/two-sum/

Description:
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums[i+1:]:
                j = nums.index(diff, i+1)
                return [i, j]
