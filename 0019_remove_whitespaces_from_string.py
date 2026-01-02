"""
Question:
---------
Write a program to remove all white spaces from a string.
"""


def remove_whitespaces(s: str) -> str:
    """
    Removes all white spaces from the given string.

    Approach:
    - Iterate through each character in the string
    - Skip the character if it is a space
    - Append all other characters to a new string

    Time Complexity: O(n)
    Space Complexity: O(n)

    :param s: Input string
    :return: String without white spaces
    """
    new_string = ""

    for ch in s:
        if ch == " ":
            continue
        else:
            new_string += ch

    return new_string


if __name__ == "__main__":
    s = "df 7 dgj9 df "

    result = remove_whitespaces(s)
    print(f"The new string is: {result}")
