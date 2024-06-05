import numpy as np
from matplotlib.patches import RegularPolygon

from Task4.geometric_figure import GeometricFigure
from Task4.shape_color import ShapeColor


class RegularNGon(GeometricFigure):
    """
    A class representing a regular n-sided polygon.

    Attributes:
        shape_name (str): The name of the shape.
        _n (int): The number of sides of the polygon.
        _a (float): The length of each side of the polygon.
        _color (ShapeColor): The color of the polygon.

    Methods:
        area(): Calculate the area of the polygon.
        __str__(): Return a string representation of the polygon.
        get_patch(): Get a matplotlib RegularPolygon patch representing the polygon.
    """

    shape_name = "RegularPolygon"

    def __init__(self, n, a, color):
        """
        Initialize the RegularNGon with the number of sides, side length, and color.

        Parameters:
            n (int): The number of sides of the polygon.
            a (float): The length of each side of the polygon.
            color (str): The color of the polygon.
        """
        super().__init__()
        self._n = n
        self._a = a
        self._color = ShapeColor(color)

    def area(self):
        """
        Calculate the area of the polygon.

        Returns:
            float: The area of the polygon.
        """
        return 0.25 * self._n * self._a ** 2 * (1 / np.tan(np.pi / self._n))

    def __str__(self):
        """
        Return a string representation of the polygon.

        Returns:
            str: A string representation of the polygon.
        """
        return (f"{RegularNGon.shape_name} "
                f"color: {self._color.color} "
                f"number of sides: {self._n} "
                f"side length: {self._a} "
                f"area: {self.area()}")

    def get_patch(self):
        """
        Get a matplotlib RegularPolygon patch representing the polygon.

        Returns:
            matplotlib.patches.RegularPolygon: A matplotlib RegularPolygon patch representing the polygon.
        """
        return RegularPolygon((0, 0), numVertices=self._n, radius=self._a / (2 * np.sin(np.pi / self._n)),
                              edgecolor=self._color.color, facecolor=self._color.color)
