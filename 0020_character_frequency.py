"""
Question:
---------
Write a program to find the frequency of each character in a string.
"""


def character_frequency(s: str) -> dict:
    """
    Finds the frequency of each character in a string.

    Approach:
    - Iterate through each character in the string
    - Use a dictionary to keep track of character counts
    - If the character is not present, initialize count to 1
    - If present, increment the count

    Time Complexity: O(n)
    Space Complexity: O(k)
        where n = length of the string
              k = number of unique characters

    :param s: Input string
    :return: Dictionary containing character frequencies
    """
    freq_dict = {}

    for ch in s:
        if ch not in freq_dict:
            freq_dict[ch] = 1
        else:
            freq_dict[ch] += 1

    return freq_dict


if __name__ == "__main__":
    s = "adccabd"

    result = character_frequency(s)
    print(f"The character frequency is: {result}")
