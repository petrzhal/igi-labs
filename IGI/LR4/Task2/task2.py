import re
import zipfile
from collections import Counter
import nltk


class TextAnalyzer:
    """
    A class to analyze text data.

    Attributes:
        filename (str): The filename of the text file to be analyzed.

    Methods:
        - read_text(): Reads the text from the specified file.
        - save_to_file(data: str, filename: str): Saves the analyzed data to a file.
        - analyze_text(): Analyzes the text data and returns the analysis results.
        - get_sentence_type(sentence: str) -> str or None: Determines the type of a sentence.
        - has_vowel_consonant_pattern(word: str) -> bool: Checks if a word follows a vowel-consonant pattern.
        - find_last_word_with_i(text: str) -> tuple: Finds the last word containing 'i' in the text.
        - exclude_words_starting_with_i(text: str) -> str: Excludes words starting with 'i' from the text.
    """
    def __init__(self, filename):
        self.filename = filename

    def read_text(self):
        """
        Read the text from the specified file.

        Returns:
            str: The text read from the file.
        """
        with open(self.filename, 'r', encoding='utf-8') as file:
            return file.read()

    @staticmethod
    def save_to_file(data, filename):
        """
        Save the analyzed data to a file.

        Parameters:
            data (str): The analyzed data to be saved.
            filename (str): The name of the file to save the data to.
        """
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(data)

    def analyze_text(self):
        """
        Analyze the text data and return the analysis results.

        Returns:
            str: The analysis results.
        """
        try:
            text = self.read_text()
            sentences = nltk.sent_tokenize(text)
            sentence_types = Counter(self.get_sentence_type(sentence) for sentence in sentences)
            sentence_count = len(sentences)
            average_sentence_length = TextAnalyzer.average_sentence_length(sentences)
            average_word_length = sum(len(word) for word in re.findall(r'\b\w+\b', text)) / len(re.findall(r'\b\w+\b', text))
            smiley_count = len(re.findall(r'[;:]-*[()\[\]]+', text))
            date_list = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
            words_with_vowel_consonant = [word for word in re.findall(r'\b\w+\b', text) if self.has_vowel_consonant_pattern(word)]
            lowercase_letters_count = sum(1 for char in text if char.islower())
            last_word_with_i, last_word_index = self.find_last_word_with_i(text)
        except Exception as e:
            print(e)
            return None

        result = f"Total sentences: {sentence_count}\n"
        result += f"Narrative sentences: {sentence_types['narrative']}\n"
        result += f"Interrogative sentences: {sentence_types['interrogative']}\n"
        result += f"Imperative sentences: {sentence_types['imperative']}\n"
        result += f"Average sentence length: {average_sentence_length:.2f} words\n"
        result += f"Average word length: {average_word_length:.2f} characters\n"
        result += f"Smiley count: {smiley_count}\n"
        result += f"Date list: {date_list}\n"
        result += f"Words with vowel-consonant pattern: {words_with_vowel_consonant}\n"
        result += f"Lowercase letters count: {lowercase_letters_count}\n"
        result += f"Last word with 'i': {last_word_with_i}, index: {last_word_index}\n"
        result += self.exclude_words_starting_with_i(text)

        self.save_to_file(result, 'result.txt')
        with zipfile.ZipFile('result.zip', 'w') as zipf:
            zipf.write('result.txt')
        return result

    @staticmethod
    def average_sentence_length(sentences):
        """
        Вычисляет среднюю длину предложения в тексте.

        :return: Средняя длина предложения.
        """
        return sum(len(sentence.split()) for sentence in sentences) / len(sentences)

    @staticmethod
    def get_sentence_type(sentence):
        """
        Determine the type of a sentence.

        Parameters:
            sentence (str): The sentence to analyze.

        Returns:
            str or None: The type of the sentence ('narrative', 'interrogative', 'imperative'), or None if the sentence is empty.
        """
        if sentence.strip().endswith('?'):
            return 'interrogative'
        elif sentence.strip().endswith('!'):
            return 'imperative'
        elif sentence.strip():
            return 'narrative'
        else:
            return None

    @staticmethod
    def has_vowel_consonant_pattern(word):
        """
        Check if a word follows a vowel-consonant pattern.

        Parameters:
            word (str): The word to analyze.

        Returns:
            bool: True if the word follows the pattern, False otherwise.
        """
        return bool(re.match(r'.*[aeiouyAEIOUY][^aeiouyAEIOUY]$', word))

    @staticmethod
    def find_last_word_with_i(text):
        """
        Find the last word containing 'i' in the text.

        Parameters:
            text (str): The text to search.

        Returns:
            tuple: A tuple containing the last word with 'i' and its index in the text.
        """
        matches = re.findall(r'\b\w*i\w*\b', text)
        if matches:
            last_match = matches[-1]
            return last_match, text.rfind(last_match) + len(last_match)
        else:
            return None, -1

    @staticmethod
    def exclude_words_starting_with_i(text):
        """
        Exclude words starting with 'i' from the text.

        Parameters:
            text (str): The text to process.

        Returns:
            str: The text with words starting with 'i' excluded.
        """
        return ' '.join(word for word in re.findall(r'\b(?!i)\w+\b', text))


class Task2:
    """
    A class to start Task2 application.

    Methods:
        - start(): Starts the Task2 application.
    """
    def start(self):
        """
        Starts the Task2 application.
        """
        result = TextAnalyzer(self.filename).analyze_text()
        print(result)


class Mixer(TextAnalyzer, Task2):
    pass

