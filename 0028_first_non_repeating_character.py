"""
File: first_non_repeating_character.py
Author: Deepak Sharma
Description:
    This program finds the first non-repeating character in a given string.

Approach:
    1. Count the frequency of each character using a dictionary.
    2. Traverse the string again to find the first character with frequency = 1.

Time Complexity:
    O(n)
    where n is the length of the input string.

Space Complexity:
    O(n)
    for storing character frequencies in a dictionary.

Example:
    Input:  "my name is deepak"
    Output: 'm'
"""


def find_first_non_repeating_character(text: str) -> str | None:
    """
    Returns the first non-repeating character in the given string.

    :param text: Input string
    :return: First non-repeating character or None if not found
    """
    frequency_map = {}

    # Step 1: Count character frequencies
    for character in text:
        frequency_map[character] = frequency_map.get(character, 0) + 1

    # Step 2: Find first non-repeating character
    for character in text:
        if frequency_map[character] == 1:
            return character

    return None


if __name__ == "__main__":
    input_string = "my name is deepak"

    result = find_first_non_repeating_character(input_string)

    if result:
        print(f"First non-repeating character: '{result}'")
    else:
        print("No non-repeating character found.")
