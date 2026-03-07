"""
Pattern 03 — Inverted Right Triangle Star Pattern

Problem:
Print an inverted right triangle star pattern of size n.

Example:
Input:
n = 4

Output:
* * * *
* * *
* *
*

Approach:
This pattern consists of n rows.

Row 1 -> n stars
Row 2 -> n-1 stars
Row 3 -> n-2 stars
...
Last Row -> 1 star

We use nested loops:
1. The outer loop controls the rows.
2. The inner loop prints stars.
3. The number of stars decreases in each row.
"""

# Take input from user
n = int(input("Enter the number of rows: "))

# Outer loop -> controls rows (decreasing order)
for row in range(n, 0, -1):

    # Inner loop -> prints stars
    for col in range(row):
        print("*", end=" ")

    # Move to next line after printing each row
    print()


"""
Time Complexity:
O(n²)

Explanation:
The total number of stars printed is:

n + (n-1) + (n-2) + ... + 1
= n(n+1)/2

Which simplifies to O(n²).

Space Complexity:
O(1)

Explanation:
No extra memory or data structures are used.
Only a few variables (n, row, col) are used.
Therefore space complexity is constant.
"""