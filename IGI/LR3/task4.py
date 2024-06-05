from collections import Counter


def count_vowel_starting_words(text):
    """
        Function for counting words that start with vowels in the text.

        Parameters:
        text (str): Input text.

        Returns:
        vowel_starting_count (int): Number of words starting with vowels.
    """
    vowels = 'aeiouAEIOU'
    vowel_starting_count = 0

    words = text.split()
    for word in words:
        if word[0] in vowels:
            vowel_starting_count += 1

    return vowel_starting_count


def count_characters(text):
    """
        Function for counting the repetitions of each character in the text.

        Parameters:
        text (str): Input text.

        Returns:
        Counter(text) (Counter): Character counter in the text.
    """
    return Counter(text)


def sort_words_after_comma(s):
    """
        Function for sorting words after a comma in a string.

        Parameters:
        s (str): Input string.

        Returns:
        words (list): Sorted list of words after the comma.
    """
    parts = s.split(",")
    words = [part.strip().split(" ")[0] for part in parts[1:] if part.strip()]
    words.sort()
    return words


def task4():
    """
        Function to perform task 4. Task 4 involves calling the functions count_vowel_starting_words,
        count_characters, and sort_words_after_comma on a certain input text.
    """
    input_text = ("So she was considering in her own mind, as well as she could, for the hot day made her feel very "
                  "sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of "
                  "getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.")

    vowel_starting_count = count_vowel_starting_words(input_text)
    print("Number of words ending with a consonant: ", vowel_starting_count)
    print("Repetitions of each character: ", count_characters(input_text))
    print("Sorted words after the comma: ", sort_words_after_comma(input_text))
