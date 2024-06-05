import random


def task5():
    """
        Function to perform task 5. Task 5 involves calling the functions input_list, print_list, and process_list.
    """
    print("Choose how to fill the list:\n 1 - Manually\n 2 - Generate randomly\n")
    choice = int(input())
    if choice == 1:
        lst = input_list()
    elif choice == 2:
        lst = list(generate_float_list())
    else:
        print("Incorrect choice")
        return
    print_list(lst)
    product, sum_positive = process_list(lst)
    print(f"Product of negative elements of the list: {product}")
    print(f"Sum of positive elements of the list, located before the maximum element: {sum_positive}")


def generate_float_list():
    count = random.randint(3, 20)
    for i in range(count):
        yield random.uniform(-100, 100)


def input_list():
    """
        Function for inputting a list from the keyboard. The size of the list and its elements are entered by the user.

        Returns:
        lst (list): List entered by the user.
    """
    while True:
        try:
            list_size = int(input("Enter the size of the list: "))
            if list_size <= 0:
                print("The size of the list must be greater than 0. Try again.")
                continue
            break
        except ValueError:
            print("Incorrect input. Try again.")

    lst = []
    for i in range(list_size):
        while True:
            try:
                element = float(input(f"Enter element {i + 1}: "))
                lst.append(element)
                break
            except ValueError:
                print("Incorrect input. Try again.")
    return lst


def process_list(lst):
    """
        Function for processing a list. Calculates the product of negative elements of the list and the sum of positive
        elements of the list, located before the maximum element.

        Parameters:
        lst (list): List for processing.

        Returns:
        product (float): Product of negative elements of the list.
        sum_positive (float): Sum of positive elements of the list, located before the maximum element.
    """
    max_element = max(lst)
    max_index = lst.index(max_element)

    product = 1
    for element in lst:
        if element < 0:
            product *= element

    sum_positive = sum(element for element in lst[:max_index] if element > 0)

    return product, sum_positive


def print_list(lst):
    """
        Function for printing a list.

        Parameters:
        lst (list): List for printing.
    """
    print("List: ", lst)
