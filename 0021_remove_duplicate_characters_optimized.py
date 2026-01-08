"""
Question:
---------
Write a program to remove duplicate characters from a string
while preserving the original order.

Optimized Approach (O(n)):
-------------------------
Use a set to track already-seen characters.
Set lookup is O(1) on average, so the overall time complexity is linear.
"""


def remove_duplicate_characters(s: str) -> str:
    """
    Removes duplicate characters from a string while maintaining order.

    Time Complexity: O(n)
        - Single pass through the string
        - O(1) average lookup using a set

    Space Complexity: O(n)
        - Extra space used by the set and result string

    :param s: Input string
    :return: String without duplicate characters
    """
    seen = set()
    result = []

    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)

    return "".join(result)


if __name__ == "__main__":
    s = "adccabd"

    output = remove_duplicate_characters(s)
    print(f"The new string is: {output}")
