"""
Program: Armstrong Number Checker
Author: Your Name
Description:
    This program checks whether a given number is an Armstrong number.
"""

def is_armstrong(number: int) -> bool:
    """
    Checks if a number is an Armstrong number.

    Args:
        number (int): Number to be checked

    Returns:
        bool: True if Armstrong number, False otherwise
    """
    original_number = number
    number_of_digits = len(str(number))
    digit_power_sum = 0

    while number > 0:
        digit = number % 10
        digit_power_sum += digit ** number_of_digits
        number //= 10

    return digit_power_sum == original_number


def main():
    num = int(input("Enter a number: "))

    if is_armstrong(num):
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")


if __name__ == "__main__":
    main()
