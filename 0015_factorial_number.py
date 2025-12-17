"""
Program: Factorial Using Recursion (Tail Recursion)
Author: Your Name
Description:
    This program calculates the factorial of a given number
    using recursion with an accumulator (tail recursion).
"""

def fact(num: int, prod: int = 1) -> int:
    """
    Calculates factorial of a number using recursion.

    Args:
        num (int): Number whose factorial is to be calculated
        prod (int): Accumulator to store intermediate result

    Returns:
        int: Factorial of the given number
    """
    if num <= 1:
        return prod

    return fact(num - 1, prod * num)


def main():
    num = int(input("Enter a number: "))

    if num < 0:
        print("Factorial is not defined for negative numbers.")
        return

    result = fact(num)
    print(f"Factorial of {num} is: {result}")


if __name__ == "__main__":
    main()
