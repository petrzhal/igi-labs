from abc import ABC, abstractmethod


class GeometricFigure(ABC):
    """
    An abstract base class for geometric figures.

    Methods:
        - area(): Abstract method to calculate the area of the geometric figure.
    """
    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the geometric figure.
        """
        pass
