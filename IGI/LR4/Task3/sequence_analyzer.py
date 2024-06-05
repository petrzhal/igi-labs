import numpy as np
from scipy import stats


class SequenceAnalyzer:
    """
    A class to analyze sequences of numerical data.

    Attributes:
        sequence (list or numpy.ndarray): The sequence of numerical data to be analyzed.

    Methods:
        - mean(): Calculate the mean of the sequence.
        - median(): Calculate the median of the sequence.
        - mode(): Calculate the mode of the sequence.
        - variance(): Calculate the variance of the sequence.
        - std_deviation(): Calculate the standard deviation of the sequence.
    """

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
