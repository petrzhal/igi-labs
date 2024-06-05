import numpy as np
import matplotlib.pyplot as plt
import math
from functools import lru_cache
from Task3.sequence_analyzer import SequenceAnalyzer


class Task3:
    """
    A class to perform Task3 operations.

    Methods:
        - sum_function(x: float, n: int) -> float: Recursive function for calculating the sum of a series.
        - plot_functions(x_values: numpy.ndarray, y_values: numpy.ndarray, label: str): Plot the functions.
        - start(): Start the Task3 application.
    """

    @staticmethod
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
            return math.pi / 2 - x
        else:
            term = ((-1) ** n) * (math.factorial(2 * n - 1) / (4 ** n * (math.factorial(n) ** 2) * (2 * n + 1))) * (x ** (2 * n + 1))
            return term + Task3.sum_function(x, n - 1)

    @staticmethod
    def plot_functions(x_values, y_values, label):
        """
        Plot the functions.

        Parameters:
            x_values (numpy.ndarray): The x values for plotting.
            y_values (numpy.ndarray): The y values for plotting.
            label (str): The label for the plot.
        """
        plt.plot(x_values, y_values, label=label)

    @staticmethod
    def start():
        """
        Start the Task3 application.
        """
        x_values = np.linspace(-1, 1, 100)

        sequence = [Task3.sum_function(x, 100) for x in x_values]

        analyzer = SequenceAnalyzer(sequence)

        print("Mean:", analyzer.mean())
        print("Median:", analyzer.median())
        print("Mode:", analyzer.mode())
        print("Variance:", analyzer.variance())
        print("Standard Deviation:", analyzer.std_deviation())

        y_values_series = sequence

        Task3.plot_functions(x_values, y_values_series, label='Series Sum')

        y_values_math = np.array([math.acos(x) for x in x_values])
        Task3.plot_functions(x_values, y_values_math, label='math.acos(x)')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.title('Series Expansion of arccos(x) vs. math.acos(x)')
        plt.savefig('plot.png')
        plt.show()
