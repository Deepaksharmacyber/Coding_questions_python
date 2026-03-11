"""
Pattern 04 — Number Triangle

Problem:
Print a number triangle pattern of size n.

Example:
Input:
n = 4

Output:
1
1 2
1 2 3
1 2 3 4

Approach:
The pattern consists of n rows.

Row 1 -> print numbers from 1 to 1
Row 2 -> print numbers from 1 to 2
Row 3 -> print numbers from 1 to 3
...
Row n -> print numbers from 1 to n

We use nested loops:
1. Outer loop controls the rows.
2. Inner loop prints numbers from 1 up to the current row number.
"""

# Take input from user
n = int(input("Enter the number of rows: "))

# Outer loop -> controls number of rows
for row in range(1, n + 1):

    # Inner loop -> prints numbers from 1 to row
    for col in range(1, row + 1):
        print(col, end=" ")

    # Move to the next line after each row
    print()


"""
Time Complexity:
O(n²)

Explanation:
Total numbers printed =

1 + 2 + 3 + ... + n
= n(n+1)/2

Which simplifies to O(n²).

Space Complexity:
O(1)

Explanation:
No extra memory or data structures are used.
Only loop variables (n, row, col) are used.
Therefore the space complexity is constant.
"""