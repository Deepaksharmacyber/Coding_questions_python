"""
File: check_string_contains_only_alphabets.py
Author: Deepak Sharma
Description:
    This program checks whether a given string contains only alphabetic
    characters (A–Z or a–z).

Approach:
    - Iterate through each character in the string.
    - Use the built-in str.isalpha() method to verify alphabetic characters.
    - If any non-alphabet character is found, return False.

Time Complexity:
    O(n)
    where n is the length of the input string.

Space Complexity:
    O(1)
    Only constant extra space is used.

Example:
    Input:  "Deepak"
    Output: True

    Input:  "Deepak123"
    Output: False
"""


def contains_only_alphabets(text: str) -> bool:
    """
    Checks if the string contains only alphabet characters.

    :param text: Input string
    :return: True if only alphabets, False otherwise
    """
    for character in text:
        if not character.isalpha():
            return False
    return True


if __name__ == "__main__":
    input_string = "Deepak"

    result = contains_only_alphabets(input_string)

    if result:
        print("The string contains only alphabets.")
    else:
        print("The string contains non-alphabet characters.")
