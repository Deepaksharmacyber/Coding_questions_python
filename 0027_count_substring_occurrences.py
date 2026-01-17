"""
File: count_substring_occurrences.py
Author: Deepak Sharma
Description:
    This program counts the number of times a substring occurs
    within a larger string using a simple sliding window approach.

Approach:
    - Iterate through the main string.
    - Compare each substring of length `len(sub)` with the target substring.
    - Increment count when a match is found.

Time Complexity:
    O(n * m)
    where:
        n = length of the main string
        m = length of the substring

Space Complexity:
    O(1)
    Only constant extra space is used.

Example:
    Input:
        s = "My name is Deepak name"
        sub = "name"
    Output:
        2
"""


def count_substring(s: str, sub: str) -> int:
    """
    Counts occurrences of a substring in a given string.

    :param s: Main string
    :param sub: Substring to search for
    :return: Number of occurrences of sub in s
    """
    count = 0
    sub_len = len(sub)

    for i in range(len(s) - sub_len + 1):
        if s[i:i + sub_len] == sub:
            count += 1

    return count


if __name__ == "__main__":
    input_string = "My name is Deepak name"
    input_sub_string = "name"

    result = count_substring(input_string, input_sub_string)
    print(f"Occurrences of '{input_sub_string}': {result}")
