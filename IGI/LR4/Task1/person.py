class Person:
    """
    A class representing a person.

    Attributes:
        last_name (str): The last name of the person.
        gender (str): The gender of the person. Defaults to None.
        height (float): The height of the person in meters. Defaults to None.
    """

    def __init__(self, last_name, gender, height):
        """
        Initialize a person object with a last name.

        Parameters:
            last_name (str): The last name of the person.
        """

        self.last_name = last_name
        self.gender = gender
        self.height = height
