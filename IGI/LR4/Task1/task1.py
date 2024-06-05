from Task1.person import Person
from Task1.serializer import Serializer


class Task1:
    """
    A class to perform various operations on a list of people and serialize/deserialize data.

    Methods:
        - start(): Starts the Task1 application.
        - average_female_height(people: list) -> float: Calculates the average height of females.
        - tallest_male_last_name(people: list) -> str or None: Finds the last name of the tallest male.
        - input_person_info(people: list, last_name: str): Prints information about a person by last name.
        - has_same_height_pair(people: list) -> bool: Checks if there is a pair of people with the same height.
    """

    def start(self):
        """
        Starts the Task1 application.
        - Creates a list of people from given data.
        - Calculates and prints the average height of females.
        - Finds and prints the last name of the tallest male.
        - Checks and prints if there is a pair of people with the same height.
        - Prompts the user to enter a last name and prints information about the person with that last name.
        - Serializes the data to CSV and pickle formats.
        - Deserializes the data from CSV and pickle formats and performs operations on the loaded data.
        """
        data_dict = [
            {'name': 'Alice', 'gender': 'male', 'height': 150},
            {'name': 'Bob', 'gender': 'female', 'height': 180},
            {'name': 'Charlie', 'gender': 'male', 'height': 160}
        ]

        people = [Person(person['name'], person['gender'], person['height']) for person in data_dict]
        print(f"Average female height: {self.average_female_height(people)}")
        print(f"Tallest male last name: {self.tallest_male_last_name(people)}")
        print(f"Is same height pair: {self.has_same_height_pair(people)}")
        last_name = input("Enter last name: ")
        self.input_person_info(people, last_name)

        serializer = Serializer(data_dict)

        serializer.save_to_csv('data.csv')
        serializer.save_to_pickle('data.pkl')

        loaded_data_csv = Serializer.load_from_csv('data.csv')
        loaded_data_pickle = Serializer.load_from_pickle('data.pkl')

        print("Search by gender 'male':", loaded_data_csv.search('gender', 'male'))
        print("Sort by name:", loaded_data_pickle.sort('name'))

    @staticmethod
    def average_female_height(people):
        """
        Calculates the average height of females in the given list of people.

        Parameters:
            people (list): A list of Person objects.

        Returns:
            float: The average height of females.
        """
        female_heights = [person.height for person in people if person.gender == 'female']
        if not female_heights:
            return 0
        return sum(female_heights) / len(female_heights)

    @staticmethod
    def tallest_male_last_name(people):
        """
        Finds the last name of the tallest male in the given list of people.

        Parameters:
            people (list): A list of Person objects.

        Returns:
            str or None: The last name of the tallest male, or None if there are no males in the list.
        """
        male_people = [person for person in people if person.gender == 'male']
        if not male_people:
            return None
        tallest_male = max(male_people, key=lambda x: x.height)
        return tallest_male.last_name

    @staticmethod
    def input_person_info(people, last_name):
        """
        Prints information about the person with the specified last name.

        Parameters:
            people (list): A list of Person objects.
            last_name (str): The last name of the person to get information about.
        """
        person = [person for person in people if person.last_name == last_name]
        if not person:
            return None
        print(f"Name: {last_name}\nGender: {person[0].gender}\nHeight: {person[0].height}")

    @staticmethod
    def has_same_height_pair(people):
        """
        Checks if there is a pair of people with the same height in the given list of people.

        Parameters:
            people (list): A list of Person objects.

        Returns:
            bool: True if there is a pair of people with the same height, False otherwise.
        """
        heights = [person.height for person in people]
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                if heights[i] == heights[j]:
                    return True
        return False
