"""
Program: Leap Year Checker
Author: Your Name
Description:
    This program checks whether a given year is a leap year or not
    based on the Gregorian calendar rules.

Leap Year Rules:
    - A year is a leap year if:
        1. It is divisible by 400
        OR
        2. It is divisible by 4 and not divisible by 100

Time Complexity:
    O(1)
    - The program performs a constant number of arithmetic operations.

Space Complexity:
    O(1)
    - The program uses a constant amount of extra memory.
"""

def is_leap_year(year: int) -> bool:
    """
    Determines whether the given year is a leap year.

    Args:
        year (int): The year to check

    Returns:
        bool: True if leap year, False otherwise

    Time Complexity:
        O(1)

    Space Complexity:
        O(1)
    """
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


def main():
    """
    Main function to take user input and display result.

    Time Complexity:
        O(1)

    Space Complexity:
        O(1)
    """
    try:
        year = int(input("Enter a year: "))

        if is_leap_year(year):
            print(f"{year} is a Leap Year ✅")
        else:
            print(f"{year} is Not a Leap Year ❌")

    except ValueError:
        print("Invalid input! Please enter a valid integer year.")


if __name__ == "__main__":
    main()
