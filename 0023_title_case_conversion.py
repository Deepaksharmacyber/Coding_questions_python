"""
Title Case Conversion in Python
--------------------------------
This file demonstrates two approaches to convert a sentence
into Title Case (capitalize the first letter of each word).

Method 1:
- Optimized, Pythonic, and efficient
- Uses a mutable list and single join

Method 2:
- Manual word-building approach
- Useful for learning string traversal
"""


# =========================================================
# Method 1: Optimized Character-Based Approach (Recommended)
# =========================================================

def title_case_method_1(input_string):
    """
    Converts a sentence to title case using a single pass.

    Time Complexity:
        O(n) — each character is processed once

    Space Complexity:
        O(n) — extra list used to store characters
    """

    result = []
    make_upper = True

    for ch in input_string:
        if ch == ' ':
            make_upper = True
            result.append(ch)
        else:
            if make_upper and 'a' <= ch <= 'z':
                result.append(chr(ord(ch) - 32))
                make_upper = False
            else:
                result.append(ch)
                make_upper = False

    return ''.join(result)


# =========================================================
# Method 2: Manual Word Construction Approach (Learning)
# =========================================================

def title_case_method_2(input_string):
    """
    Converts a sentence to title case by manually building words.

    Time Complexity:
        O(n²) — due to repeated string concatenation

    Space Complexity:
        O(n) — additional strings used to build result
    """

    input_string = ' ' + input_string + ' '
    new_string = ''
    old_string = ''

    for ch in input_string:
        if ch == ' ':
            new_string += ' ' + old_string
            old_string = ''
        else:
            if old_string == '' and ('a' <= ch <= 'z'):
                old_string += chr(ord(ch) - 32)
            else:
                old_string += ch

    return new_string.strip()


# =========================================================
# Example Usage
# =========================================================

if __name__ == "__main__":
    sentence = "my name is deepak"

    print("Original String:")
    print(sentence)

    print("\nMethod 1 Output (Optimized):")
    print(title_case_method_1(sentence))

    print("\nMethod 2 Output (Manual):")
    print(title_case_method_2(sentence))
