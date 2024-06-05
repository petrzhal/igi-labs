import numpy as np


class Sequence:
    def __init__(self, sequence):
        """
        Initialize the SequenceAnalyzer with a sequence of numerical data.

        Parameters:
            sequence (list or numpy.ndarray): The sequence of numerical data to be analyzed.
        """
        self.sequence = sequence

    def mean(self):
        """
        Calculate the mean of the sequence.

        Returns:
            float: The mean of the sequence.
        """
        return np.mean(self.sequence)

    def median(self):
        """
        Calculate the median of the sequence.

        Returns:
            float: The median of the sequence.
        """
        return np.median(self.sequence)

    def mode(self):
        """
        Calculate the mode of the sequence.

        Returns:
            int or float or None: The mode of the sequence, or None if the sequence has no mode.
        """
        mode_result = stats.mode(self.sequence)
        if isinstance(mode_result.mode, np.ndarray) and len(mode_result.mode) > 0:
            return mode_result.mode[0]
        else:
            return None

    def variance(self):
        """
        Calculate the variance of the sequence.

        Returns:
            float: The variance of the sequence.
        """
        return np.var(self.sequence)

    def std_deviation(self):
        """
        Calculate the standard deviation of the sequence.

        Returns:
            float: The standard deviation of the sequence.
        """
        return np.std(self.sequence)

class Task5:
    """
    A class to perform Task5 operations.

    Methods:
        start(): Start the Task5 application.
    """

    @staticmethod
    def start():
        """
        Start the Task5 application.
        """
        n = 5
        m = 4
        A = np.random.randint(1, 100, size=(n, m))
        print("Original matrix A:\n", A)

        max_first_col = np.max(A[:, 0])
        max_last_col = np.max(A[:, -1])

        idx_max_first_col = np.argmax(A[:, 0])
        idx_max_last_col = np.argmax(A[:, -1])

        A[idx_max_first_col, 0], A[idx_max_last_col, -1] = max_last_col, max_first_col

        print("\nMatrix A with the largest elements swapped in the first and last columns:\n", A)

        correlation_coefficient = np.corrcoef(A[:, 0], A[:, -1])[0, 1]
        print("\nValue of the correlation coefficient between elements of the first and last columns:", round(correlation_coefficient, 2))


class SequenceAnalyzer2(Sequence, Task5):
    pass
