from functools import lru_cache
import math


@lru_cache(maxsize=None)
def sum_function(x, n):
    """
        Recursive function for calculating the sum of a series.

        Parameters:
        x (float): The value of x for which the series sum is calculated.
        n (int): The number of series terms to sum.

        Returns:
        float: The sum of the first n terms of the series for the given x.
    """
    if n == 0:
        return x
    result = ((math.factorial(2 * n) / ((4 ** n) * (math.factorial(n) ** 2) * (2 * n + 1))) * (x ** (2 * n + 1)))
    return (math.pi / 2) - (result + sum_function(x, n - 1))


def task1():
    """
        Function to perform the main task. It asks the user to input the values of x and eps,
        calculates the function value using sum_function and compares it with math.acos(x).
        The results are displayed on the screen.

        Parameters: None

        Returns: Nothing
    """
    x = float(input("Enter x: "))
    eps = float(input("Enter precision: "))
    arccos = math.acos(x)

    max_iter = 500
    n = 0
    while n < max_iter:
        value = sum_function(x, n)
        if abs(arccos - value) < eps:
            break
        n += 1
    print("x | n | F(x) | Math F(x) | eps")
    print(f"{x} | {n} | {value} | {arccos} | {eps}")
