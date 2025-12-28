"""
Question:
---------
Write a program to swap two variables without using a third variable.

This file demonstrates two approaches:
1. Pythonic tuple unpacking
2. Bitwise XOR method

Both approaches swap the values of two variables without using any extra variable.
"""


def swap_using_tuple(a, b):
    """
    Swap two variables using Python tuple unpacking.

    This is the most Pythonic and readable approach.

    Time Complexity: O(1)
    Space Complexity: O(1)

    :param a: First variable
    :param b: Second variable
    :return: Swapped values (b, a)
    """
    a, b = b, a
    return a, b


def swap_using_xor(a, b):
    """
    Swap two variables using the XOR bitwise operator.

    This method works only for integers and does not use extra memory.

    Time Complexity: O(1)
    Space Complexity: O(1)

    :param a: First integer
    :param b: Second integer
    :return: Swapped values (a, b)
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


if __name__ == "__main__":
    x = 10
    y = 20

    print("Original Values:")
    print(f"x = {x}, y = {y}")

    # Method 1: Tuple Unpacking
    x, y = swap_using_tuple(x, y)
    print("\nAfter swapping using tuple unpacking:")
    print(f"x = {x}, y = {y}")

    # Method 2: XOR Swap
    x, y = swap_using_xor(x, y)
    print("\nAfter swapping using XOR method:")
    print(f"x = {x}, y = {y}")
