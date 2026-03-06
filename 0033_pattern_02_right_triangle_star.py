"""
Pattern 02 — Right Triangle Star Pattern

Problem:
Print a right triangle star pattern of size n.

Example:
Input:
n = 4

Output:
*
* *
* * *
* * * *

Approach:
The pattern consists of n rows.

Row 1 -> 1 star
Row 2 -> 2 stars
Row 3 -> 3 stars
Row n -> n stars

We use nested loops:
- Outer loop controls rows
- Inner loop prints stars equal to the row number
"""

# Take input from user
n = int(input("Enter the number of rows: "))

# Outer loop -> number of rows
for row in range(1, n + 1):

    # Inner loop -> number of stars per row
    for col in range(row):
        print("*", end=" ")

    # Move to next line after each row
    print()


"""
Time Complexity:
O(n²)

Explanation:
Total stars printed = 1 + 2 + 3 + ... + n
= n(n+1)/2 ≈ O(n²)

Space Complexity:
O(1)

Explanation:
No extra memory used, only loop variables.
"""