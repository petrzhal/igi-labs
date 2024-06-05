class ShapeColor:
    """
    A class representing the color of a shape.

    Attributes:
        _color (str): The color of the shape.

    Methods:
        color(): Get the color of the shape.
    """

    def __init__(self, color):
        """
        Initialize the ShapeColor with a color.

        Parameters:
            color (str): The color of the shape.
        """
        self._color = color

    @property
    def color(self):
        """
        Get the color of the shape.

        Returns:
            str: The color of the shape.
        """
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @color.deleter
    def color(self):
        del self._color
