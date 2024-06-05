import string


def count_punctuation(input_string):
    """
        Function for counting the number of punctuation marks in a string.

        Parameters:
        input_string (str): The string in which to count punctuation marks.

        Returns:
        int: The number of punctuation marks in input_string.
    """
    punctuation_count = 0
    for char in input_string:
        if char in string.punctuation:
            punctuation_count += 1
    return punctuation_count


def task3():
    """
        Function to perform the main task. It asks the user to input a string,
        calculates the number of punctuation marks and spaces in this string and displays the results on the screen.

        Parameters: None

        Returns: Nothing
    """
    user_input = input("Enter a string: ")
    print("Number of punctuation marks in the string:", count_punctuation(user_input))
    print(f"Number of spaces: {user_input.count(' ')}")
