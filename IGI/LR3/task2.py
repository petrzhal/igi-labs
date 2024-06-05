def task2():
    """
        Function for calculating the arithmetic mean of even numbers entered by the user.

        The function asks the user to input integers until 0 is entered.
        Then it calculates the arithmetic mean of all entered even numbers and displays it on the screen.

        Parameters: None

        Returns: Nothing
    """
    count = 0
    sum = 0
    average = 0
    while True:
        num = int(input("Enter an integer (Enter 0 to finish): "))

        if num == 0:
            break
        elif num % 2 == 0:
            count += 1
            sum += num
            average = sum / count

    print(f"Arithmetic mean of entered even numbers: {average}")
