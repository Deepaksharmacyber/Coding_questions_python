"""
Pattern 06 — Continuous Number Triangle

Problem:
Print a triangle where numbers increase continuously across rows.

Example:
Input:
n = 4

Output:
1
2 3
4 5 6
7 8 9 10

Approach:
The pattern contains n rows.

Row 1 -> print 1 number
Row 2 -> print 2 numbers
Row 3 -> print 3 numbers
...
Row n -> print n numbers

Instead of restarting numbers in every row, we maintain
a variable `count` that increments continuously.
"""

# Take input from user
n = int(input("Enter the number of rows: "))

# Initialize number counter
count = 1

# Outer loop -> controls rows
for row in range(1, n + 1):

    # Inner loop -> prints numbers for the current row
    for col in range(row):
        print(count, end=" ")
        count += 1

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
Only a few variables (n, row, col, count) are used.
No additional memory or data structures are required.
Therefore the space complexity is constant.
"""