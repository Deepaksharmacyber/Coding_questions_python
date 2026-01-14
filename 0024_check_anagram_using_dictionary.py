"""
Program: Check if two strings are anagrams using dictionary
Author: Deepak Sharma

Description:
Two strings are anagrams if they contain the same characters
with the same frequency, irrespective of order.

Time Complexity:
O(n), where n is the length of the strings.
- One pass to count characters in the first string
- One pass to count characters in the second string
- Dictionary comparison also takes O(n)

Space Complexity:
O(n), where n is the number of unique characters.
- Two dictionaries are used to store character frequencies
"""

def are_anagrams(s1, s2):
    # If lengths differ, they cannot be anagrams
    if len(s1) != len(s2):
        return False

    d1 = {}
    d2 = {}

    # Count frequency of characters in first string
    for ch in s1:
        if ch not in d1:
            d1[ch] = 1
        else:
            d1[ch] += 1

    # Count frequency of characters in second string
    for ch in s2:
        if ch not in d2:
            d2[ch] = 1
        else:
            d2[ch] += 1

    # Compare both dictionaries
    return d1 == d2


# ---- Driver code ----
s1 = "listen"
s2 = "slient"

if are_anagrams(s1, s2):
    print("true")
else:
    print("no")
