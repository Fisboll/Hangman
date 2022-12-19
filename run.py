import random
from one_word import word_list as word_list_one
from two_word import word_list as word_list_two

class text_colors:
    BLUE = '\033[38;5;159m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'


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
    print(text_colors.BLUE + """ Welcome to
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
""" + text_colors.WHITE)

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
            return word.upper()
            difficulty_selected = True
        elif difficulty == "VH":
            tries = 6
            print("You chose Very Hard difficulty. You have ", tries, "tries")
            word = random.choice(word_list_two)
            return word.upper()
            difficulty_selected = True
        else:
            print(difficulty, "is not a difficulty")

    print(display_hangman(tries))
    print(word_completion)
    print(" \n ")
    while not guessed and tries > 0:
        guess = input("please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
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
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guesed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
            print(display_hangman(tries))
            print(word_completion)
            print(" \n ")
    if guessed:
        print(text_colors.GREEN + """Congrats, you guessed the word!
 ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄                 ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄    
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░▌               ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌   
▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░▌               ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀    
▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌               ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌▐░▌             
▐░▌   ▄   ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░▌               ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄▄▄    
▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░▌               ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌   
▐░▌ ▐░▌░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░▌               ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌   ▐░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀    
▐░▌▐░▌ ▐░▌▐░▌▐░▌          ▐░▌          ▐░▌               ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌▐░▌             
▐░▌░▌   ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄  ▄ 
▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░▌
 ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀ 
                                                                                                                
 ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄       ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄                              
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌                             
▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌     ▐░▌       ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌                             
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌       ▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌                             
▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌   ▄   ▐░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌                             
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌  ▐░▌  ▐░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌                             
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌ ▐░▌░▌ ▐░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌                             
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌▐░▌ ▐░▌▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌                             
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌░▌   ▐░▐░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌                             
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌                             
      ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀                              
""" + text_colors.White)
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    """
    Displays hangman graphic based on lives left
    """
    stages = [ 
        # final state: head, torso, both arms, and both legs
        """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        / \\
        |\\
        ========
        """,
        # head, torso, both arms, and one leg
        """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        /
        |\\
        ========
        """,
        # head, torso, and both arms
        """
        __________
        |/        |
        |         O
        |        /|\\
        |         |
        |
        |\\
        ========
        """,
        # head, torso, and one arm
        """
        __________
        |/        |
        |         O
        |        /|
        |         |
        |
        |\\
        ========
        """,
        # head, neck and torso
        """
        __________
        |/        |
        |         O
        |         |
        |         |
        |
        |\\
        ========
        """,
        # head and neck
        """
        __________
        |/        |
        |         O
        |
        |
        |
        |\\
        ========
        """,
        """
        __________
        |/
        |
        |
        |
        |
        |\\
        ========
        """,
        """
        __________
        |/
        |
        |
        |
        |
        |
        ========
        """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("play again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()