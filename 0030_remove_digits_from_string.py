"""
File: remove_digits_from_string.py
Author: Deepak Sharma
Description:
    This program removes all numeric digits from a given string and
    returns the resulting string containing only non-digit characters.

Approach:
    - Iterate through each character in the input string.
    - Check if the character is a digit using str.isdigit().
    - Append only non-digit characters to the result list.
    - Join the list to form the final string.

Time Complexity:
    O(n)
    where n is the length of the input string.

Space Complexity:
    O(n)
    A new string is created to store the filtered characters.

Example:
    Input:  "My name is Deepak123"
    Output: "My name is Deepak"
"""


def remove_digits(text: str) -> str:
    """
    Removes all digits from the given string.

    :param text: Input string
    :return: String without digits
    """
    result_characters = []

    for character in text:
        if not character.isdigit():
            result_characters.append(character)

    return "".join(result_characters)


if __name__ == "__main__":
    input_string = "My name is Deepak123"

    cleaned_string = remove_digits(input_string)
    print(f"String after removing digits: {cleaned_string}")
