import random
from one_word import word_list as word_list_one


def get_word():
    """
    Fetches random word from words.py and returns it in capital letters
    """
    word = random.choice(word_list_one)
    return word.upper()