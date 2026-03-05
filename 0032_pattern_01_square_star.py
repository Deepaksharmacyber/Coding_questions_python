"""
Pattern 01 — Square Star Pattern

Problem:
Print a square star pattern of size n x n.

Example:
Input:
n = 4

Output:
* * * *
* * * *
* * * *
* * * *

Approach:
The pattern consists of n rows and n columns.

1. The outer loop controls the number of rows.
2. The inner loop prints stars for each column.
3. After printing stars for a row, we move to the next line.
"""

# Take input from user
n = int(input("Enter the size of the square: "))

# Outer loop -> controls number of rows
for row in range(n):

    # Inner loop -> prints stars for each column
    for col in range(n):
        print("*", end=" ")

    # Move to the next line after printing one row
    print()


"""
Time Complexity:
O(n²)

Explanation:
The outer loop runs n times and the inner loop also runs n times.
Total operations = n * n = n².

Space Complexity:
O(1)

Explanation:
No additional data structures are used.
Only a few variables (n, row, col) are used.
Therefore the space usage is constant.
"""