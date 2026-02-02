"""
File: replace_vowels_with_special_character.py
Author: Deepak Sharma
Description:
    This program replaces all vowels in a given string with a specified
    special character.

Approach:
    - Iterate through each character in the input string.
    - If the character is a vowel (uppercase or lowercase), replace it with
      the special character.
    - Otherwise, keep the character unchanged.

Time Complexity:
    O(n)
    where n is the length of the input string.

Space Complexity:
    O(n)
    A new string is created to store the modified result.

Example:
    Input:  "My name is Deepak"
    Output: "My n$m$ $s D$$p$k"
"""


def replace_vowels(text: str, replacement_char: str) -> str:
    """
    Replaces all vowels in the given string with the specified character.

    :param text: Input string
    :param replacement_char: Character to replace vowels with
    :return: Modified string
    """
    vowels = set("aeiouAEIOU")
    result_characters = []

    for character in text:
        if character in vowels:
            result_characters.append(replacement_char)
        else:
            result_characters.append(character)

    return "".join(result_characters)


if __name__ == "__main__":
    input_string = "My name is Deepak"
    special_character = "$"

    modified_string = replace_vowels(input_string, special_character)
    print(f"Modified string: {modified_string}")
