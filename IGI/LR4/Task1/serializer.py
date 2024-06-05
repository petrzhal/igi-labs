import csv
import pickle


class Serializer:
    """
    A class to serialize/deserialize data to/from CSV and pickle formats.
    """

    def __init__(self, data):
        """
        Initialize the Serializer with data.

        Parameters:
            data (list): The data to be serialized/deserialized.
        """

        self.data = data

    def save_to_csv(self, filename):
        """
        Serialize data to a CSV file.

        Parameters:
            filename (str): The name of the CSV file to save the data to.
        """

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.data[0].keys())
            writer.writeheader()
            writer.writerows(self.data)

    @classmethod
    def load_from_csv(cls, filename):
        """
        Deserialize data from a CSV file.

        Parameters:
            filename (str): The name of the CSV file to load data from.

        Returns:
            Serializer: An instance of Serializer containing the deserialized data.
        """

        data = []
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(dict(row))
        return cls(data)

    def save_to_pickle(self, filename):
        """
        Serialize data to a pickle file.

        Parameters:
            filename (str): The name of the pickle file to save the data to.
        """

        with open(filename, 'wb') as picklefile:
            pickle.dump(self.data, picklefile)

    @classmethod
    def load_from_pickle(cls, filename):
        """
        Deserialize data from a pickle file.

        Parameters:
            filename (str): The name of the pickle file to load data from.

        Returns:
            Serializer: An instance of Serializer containing the deserialized data.
        """

        with open(filename, 'rb') as picklefile:
            data = pickle.load(picklefile)
        return cls(data)

    def search(self, key, value):
        """
        Search for items in the data with a specific key-value pair.

        Parameters:
            key (str): The key to search for.
            value: The value to search for associated with the key.

        Returns:
            list: A list of items matching the search criteria.
        """

        return [item for item in self.data if item.get(key) == value]

    def sort(self, key):
        """
        Sort the data based on a specified key.

        Parameters:
            key (str): The key to sort the data by.

        Returns:
            list: The sorted list of items.
        """

        return sorted(self.data, key=lambda x: x.get(key))
