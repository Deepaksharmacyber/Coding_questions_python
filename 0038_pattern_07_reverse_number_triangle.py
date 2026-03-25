"""
Pattern 07 — Reverse Number Triangle

Problem:
Print a reverse number triangle pattern.

Example:
Input:
n = 4

Output:
1 2 3 4
1 2 3
1 2
1

Approach:
The pattern contains n rows.

Row 1 -> print numbers from 1 to n
Row 2 -> print numbers from 1 to n-1
Row 3 -> print numbers from 1 to n-2
...
Last row -> print 1

We use nested loops:
1. The outer loop controls rows in decreasing order.
2. The inner loop prints numbers from 1 up to the current row length.
"""

# Take input from user
n = int(input("Enter the number of rows: "))

# Outer loop -> controls rows in decreasing order
for row in range(n, 0, -1):

    # Inner loop -> prints numbers from 1 to current row
    for col in range(1, row + 1):
        print(col, end=" ")

    # Move to next line
    print()


"""
Time Complexity:
O(n²)

Explanation:
Total numbers printed =

n + (n-1) + (n-2) + ... + 1
= n(n + 1) / 2

Which simplifies to O(n²).

Space Complexity:
O(1)

Explanation:
No additional memory is used.
Only loop variables (n, row, col) are used.
"""