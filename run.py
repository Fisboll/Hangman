import random
from one_word import word_list as word_list_one


def get_word():
    """
    Fetches random word from words.py and returns it in capital letters
    """
    word = random.choice(word_list_one)
    return word.upper()
    

def play(word):
    """
    displaying word for each turn, will run until
    user guesses word or runs out of tries
    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 8
    print(f"""{colored.fg(124)} Welcome to
    __   ___   ____   _____  ___   _        ___
   /  ] /   \ |    \ / ___/ /   \ | |      /  _]
  /  / |     ||  _  (   \_ |     || |     /  [_
 /  /  |  O  ||  |  |\__  ||  O  || |___ |    _]
/   \_ |     ||  |  |/  \ ||     ||     ||   [_
\     ||     ||  |  |\    ||     ||     ||     |
 \____| \___/ |__|__| \___| \___/ |_____||_____|
 __ __   ____  ____    ____  ___ ___   ____  ____
|  |  | /    ||    \  /    ||   |   | /    ||    \\
|  |  ||  o  ||  _  ||   __|| _   _ ||  o  ||  _  |
|  _  ||     ||  |  ||  |  ||  \_/  ||     ||  |  |
|  |  ||  _  ||  |  ||  |_ ||   |   ||  _  ||  |  |
|  |  ||  |  ||  |  ||     ||   |   ||  |  ||  |  |
|__|__||__|__||__|__||___,_||___|___||__|__||__|__|
{colored.attr('reset')}""")

    difficulty_selected = False
    while difficulty_selected is False:
        difficulty = input("""Please select difficulty:
E = Easy, M = Medium, H = Hard: """).upper()
        if difficulty == "E":
            tries = 8
            print("You chose Easy difficulty. You have ", tries, "tries.")
            difficulty_selected = True
        elif difficulty == "M":
            tries = 6
            print("You chose Medium difficulty. You have ", tries, "tries")
            difficulty_selected = True
        elif difficulty == "H":
            tries = 4
            print("You chose Hard difficulty. You have ", tries, "tries")
            difficulty_selected = True
        else:
            print(difficulty, "is not a difficulty")