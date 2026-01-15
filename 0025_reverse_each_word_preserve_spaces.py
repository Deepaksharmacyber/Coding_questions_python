"""
File: reverse_each_word_preserve_spaces.py

Problem:
Reverse each word in a string while preserving all spaces
(leading, trailing, and multiple spaces between words).

Example:
Input:  "  My   name is  deepak "
Output: "  yM   eman si  kapeed "

Approach:
- Traverse the string character by character
- Reverse characters of each word manually
- When a space is encountered, append the reversed word and the space
- This approach preserves the exact spacing of the input

Time Complexity:
O(n)
- Each character in the string is processed once

Space Complexity:
O(n)
- Extra space is used to store the resulting string
"""

def reverse_each_word_preserve_spaces(s: str) -> str:
    result = ""
    word = ""

    for ch in s:
        if ch != " ":
            # Prepend character to reverse the current word
            word = ch + word
        else:
            # Append reversed word and the space
            result += word + ch
            word = ""

    # Append the last reversed word (if any)
    return result + word


# ---------------- Driver Code ----------------
if __name__ == "__main__":
    test_strings = [
        "My name is deepak",
        "  My   name is  deepak ",
        "Hello",
        "   ",
        ""
    ]

    for s in test_strings:
        print(f"Input : '{s}'")
        print(f"Output: '{reverse_each_word_preserve_spaces(s)}'")
        print("-" * 40)
