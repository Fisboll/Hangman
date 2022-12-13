from cgitb import reset
from curses.ascii import isalpha
from doctest import COMPARISON_FLAGS
import random
from one_word import word_list
import controllers

def get_word():
    """
    Fetches random word from words.py and returns it in capital letters
    """
    word = random.choice(word_list)
    return word.upper()

