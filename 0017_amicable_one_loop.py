# amicable_one_loop_simple.py
"""
Compute whether two numbers are amicable using a single loop up to max(n1,n2)//2.

Time Complexity: O(max(n1, n2))
Space Complexity: O(1)
"""

def are_amicable(n1: int, n2: int) -> bool:
    if n1 <= 0 or n2 <= 0:
        return False

    sum1 = 0
    sum2 = 0
    limit = max(n1, n2) // 2  # no proper divisor > n//2 except the number itself

    for i in range(1, limit + 1):
        if i <= n1 // 2 and n1 % i == 0:
            sum1 += i
        if i <= n2 // 2 and n2 % i == 0:
            sum2 += i

    return sum1 == n2 and sum2 == n1


if __name__ == "__main__":
    n1 = 220
    n2 = 284
    print(f"{n1} and {n2} amicable? -> {are_amicable(n1, n2)}")