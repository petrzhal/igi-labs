from matplotlib import pyplot as plt
from Task4.regular_n_gon import RegularNGon


class Task4:
    """
    A class to generate and plot regular polygons.

    Methods:
        start(): Start the Task4 application.
    """

    @staticmethod
    def start():
        """
        Start the Task4 application.
        """
        n = int(input("Enter the number of sides (n) of the polygon: "))
        a = float(input("Enter the length of each side (a) of the polygon: "))
        color = input("Enter the color of the polygon: ")

        if n < 3:
            print("Error: Number of sides must be 3 or more.")
            return
        if a <= 0:
            print("Error: Length of each side must be greater than zero.")
            return
        try:
            fig, ax = plt.subplots()

            polygon = RegularNGon(n, a, color)
            ax.add_patch(polygon.get_patch())
        except ValueError:
            print("Invalid color")
            return
        ax.set_aspect('equal', 'box')
        ax.set_xlim(-a * 1.1, a * 1.1)
        ax.set_ylim(-a * 1.1, a * 1.1)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title(f'Regular {n}-gon')

        plt.show()
        fig.savefig('regular_polygon.png')
