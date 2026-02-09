"""
Problem: Move Zeroes to End of Array

Description:
Given an integer array, move all 0's to the end of the array
while maintaining the relative order of the non-zero elements.
The operation must be performed in-place without using extra space.

Example:
Input:  [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]

Approach:
- Use a two-pointer technique.
- One pointer (`write_index`) tracks the position to place the next non-zero element.
- First pass moves all non-zero elements to the front.
- Second pass fills the remaining positions with zeros.

Time Complexity:
- O(n), where n is the length of the array.
  (Two linear passes over the array, constants ignored)

Space Complexity:
- O(1), in-place modification with constant extra space.
"""


def move_zeroes(nums):
    write_index = 0

    # First pass: move non-zero elements forward
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[write_index] = nums[i]
            write_index += 1

    # Second pass: fill remaining positions with zeros
    for i in range(write_index, len(nums)):
        nums[i] = 0


# Example usage
input_array = [0, 1, 0, 3, 12]
move_zeroes(input_array)
print(input_array)