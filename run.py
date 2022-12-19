import random
from one_word import word_list as word_list_one
from two_word import word_list as word_list_two


def get_word():
    """
    Fetches random word from one_word.py and returns it in capital letters
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
E = Easy, M = Medium, H = Hard: VH = Very Hard """).upper()
        if difficulty == "E":
            tries = 8
            print("You chose Easy difficulty. You have ", tries, "tries.")
            difficulty_selected = True
        elif difficulty == "M":
            tries = 6
            print("You chose Medium difficulty. You have ", tries, "tries")
            difficulty_selected = True
        elif difficulty == "H":
            tries = 8
            print("You chose Hard difficulty. You have ", tries, "tries")
            word = random.choice(word_list_two)
            difficulty_selected = True
        elif difficulty == "VH":
            tries = 6
            print("You chose Very Hard difficulty. You have ", tries, "tries")
            word = random.choice(word_list_two)
            difficulty_selected = True
        else:
            print(difficulty, "is not a difficulty")¨

    print(display_hangman(tries))
    print(word_completion)
    print(" \n ")
    while not guessed and tries > 0:
        guess = input("please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha()
            if guess in guessed_letters:
                print("Whoops! You have already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word! Try again!")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Great Job", guess, "is a correct letter!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [
                    i for i, letter in enumerate(word)
                    if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                        word_completion = "",join(word_as_list)
                        if "_" not in word_completion:
                            guessed = True
        
        elif len(guess) == len(word) and guess.isalpha()

        else:
            print("Not a valid guess.")
            print(display_hangman(tries))
            print(word_completion)
            print(" \n ")