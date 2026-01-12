"""
Question:
---------
Write a program to find the longest word in a sentence.

The solution does not use built-in split().
It processes the string character by character.
"""


def longest_word(sentence: str) -> str:
    """
    Finds the longest word in a sentence.

    Approach:
    - Traverse the sentence character by character
    - Build words manually when characters are not spaces
    - Track the longest word based on length

    Time Complexity: O(n)
        where n is the length of the sentence

    Space Complexity: O(n)
        for storing words temporarily

    :param sentence: Input sentence
    :return: Longest word in the sentence
    """
    sentence += " "  # To process the last word
    current_word = ""
    longest_word = ""

    for ch in sentence:
        if ch != " ":
            current_word += ch
        else:
            if len(current_word) > len(longest_word):
                longest_word = current_word
            current_word = ""

    return longest_word


if __name__ == "__main__":
    s = "hello deepak world"

    result = longest_word(s)
    print(f"The longest word is: {result}")
