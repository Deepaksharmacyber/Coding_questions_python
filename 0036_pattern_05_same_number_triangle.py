"""
Pattern 05 — Same Number Triangle

Problem:
Print a triangle where each row contains the same number
repeated as many times as the row number.

Example:
Input:
n = 4

Output:
1
2 2
3 3 3
4 4 4 4

Approach:
The pattern contains n rows.

Row 1 -> print 1 time the number 1
Row 2 -> print 2 times the number 2
Row 3 -> print 3 times the number 3
...
Row n -> print n times the number n

We use nested loops:
1. The outer loop controls the number of rows.
2. The inner loop prints the row number multiple times.
"""

# Take input from user
n = int(input("Enter the number of rows: "))

# Outer loop -> controls rows
for row in range(1, n + 1):

    # Inner loop -> prints the same number 'row' times
    for col in range(row):
        print(row, end=" ")

    # Move to next line after each row
    print()


"""
Time Complexity:
O(n²)

Explanation:
Total numbers printed =

1 + 2 + 3 + ... + n
= n(n + 1) / 2

Which simplifies to O(n²).

Space Complexity:
O(1)

Explanation:
No extra memory or data structures are used.
Only loop variables (n, row, col) are used.
Therefore the space complexity is constant.
"""