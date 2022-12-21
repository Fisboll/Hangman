import random
from one_word import word_list as word_list_one
from two_word import word_list as word_list_two


class text_colors:
    """
    adds different color to wining and end screen and intro.
    """
    BLUE = '\033[38;5;159m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m'


class game_settings:
    """
    Sets the game's lives and word count
    """
    def __init__(self, lives, words):
        self.lives = lives
        self.hidden = ""
        if words == "one":
            self.get_word()
        else:
            self.get_word_two()

    def get_word(self):
        """
        Fetches random word from one_word.py and returns it in capital letters
        """
        self.word = random.choice(word_list_one).upper()
        self.hidden = "_" * len(self.word)

    def get_word_two(self):
        """
        Fetches random word from two_word.py and returns it
        """
        word = random.choice(word_list_two).upper()
        choosen_word = word.split("-")
        print(choosen_word)
        first_hidden = "_" * len(choosen_word[0])
        second_hidden = "_" * len(choosen_word[1])
        print(first_hidden, second_hidden)
        self.word = choosen_word[0] + " " + choosen_word[1]
        self.hidden = first_hidden + " " + second_hidden


def intro_logo():
    """
    intro Logo. Shows up when you start the game.
    """
    print(
        text_colors.BLUE
        + """ Welcome to
 _______                       _
(  _____)                     | |
| /      ___  ____   ___  ___ | | _____
| |     / _ \|  _ \ /___)/ _ \| || ___ |
| |____| |_| | | | |___ | |_| | || ____|
 \______)___/|_| |_(___/ \___/ \_)_____)

 _ 
| |
| |__  _____ ____   ____ ____  _____ ____
|  _ \(____ |  _ \ / _  |    \(____ |  _ \ 
| | | / ___ | | | ( (_| | | | / ___ | | | |
|_| |_\_____|_| |_|\___ |_|_|_\_____|_| |_|
                  (_____|
"""
        + text_colors.WHITE
    )


def play(game_settings):
    """
    displaying word for each turn, will run until
    user guesses word or runs out of tries
    """
    word_completion = game_settings.hidden
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = game_settings.lives

    print(game_settings.word)

    print(display_hangman(tries))
    print(word_completion)
    print(" \n ")
    while not guessed and tries > 0:
        guess = input("please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Whoops! You have already guessed the letter", guess)
            elif guess not in game_settings.word:
                print(guess, "is not in the word! Try again!")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Great Job!", guess, "is a correct letter!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [
                    i for i, letter in enumerate(
                        game_settings.word) if letter == guess
                ]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(game_settings.word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guesed the word", guess)
            elif guess != game_settings.word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
        elif len(guess) != len(game_settings.word):
            print("Your guess does not have the right amount of letters!")
        else:
            guessed = True
            word_completion = game_settings.word

        print("Woops! Please enter a letter or word! :)")
        print(display_hangman(tries))
        print(word_completion)
        print(f"There are {len(game_settings.word)} letters in this word!")
        print("\n")
    if guessed:
        win_game()
    else:
        print(
            "Sorry, you ran out of tries. The word was "
            + game_settings.word
            + "\n Maybe next time!"
        )
        lose_game()


def display_hangman(tries):
    """
    Display Hangman figures depending on lives.
    """
    stages = [  # final state: head, torso, both arms, and both legs
                """
                    --------
                    |      |
                    |      O
                    |     \|/
                    |      |
                    |     / \.
                    - """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |
                   -
                """,
                # head, neck and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head and neck
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # rope added
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |
                   |
                   |
                   |
                   |
                   -
                """,
    ]
    return stages[tries]


def win_game():
    """
    Displays when the user wins the game
    """
    print(
        text_colors.GREEN
        + """Congrats, you guessed the word!
 __    __    ___  _      _          ___     ___   ____     ___
|  |__|  |  /  _]| |    | |        |   \   /   \ |    \   /  _]
|  |  |  | /  [_ | |    | |        |    \ |     ||  _  | /  [_
|  |  |  ||    _]| |___ | |___     |  D  ||  O  ||  |  ||    _]
|  `  '  ||   [_ |     ||     |    |     ||     ||  |  ||   [_
 \      / |     ||     ||     |    |     ||     ||  |  ||     |
  \_/\_/  |_____||_____||_____|    |_____| \___/ |__|__||_____|

|  |  | /   \ |  |  |    |  |__|  ||    ||    \ |  |
|  |  ||     ||  |  |    |  |  |  | |  | |  _  ||  |
|  ~  ||  O  ||  |  |    |  |  |  | |  | |  |  ||__|
|___, ||     ||  :  |    |  `  '  | |  | |  |  | __
|     ||     ||     |     \      /  |  | |  |  ||  |
|____/  \___/  \__,_|      \_/\_/  |____||__|__||__|
"""
        + text_colors.WHITE
    )


def lose_game():
    """
    Displays when the user loses the game
    """
    print(
        text_colors.RED
        + """
                          
    ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███
   ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
  ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
  ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
  ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
   ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
   ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
   ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░
    ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░
                                                      ░
                """
        + text_colors.WHITE
    )


def select_difficulty():

    difficulty_selected = False
    while difficulty_selected is False:
        difficulty = input(
            """Please select difficulty:
E = Easy, M = Medium, H = Hard: VH = Very Hard """
        ).upper()
        if difficulty == "E":
            tries = 8
            print("You chose Easy difficulty. You have ", tries, "tries.")
            difficulty_selected = True
            player = game_settings(8, "one")
            return player
        elif difficulty == "M":
            tries = 6
            print("You chose Medium difficulty. You have ", tries, "tries")
            difficulty_selected = True
            player = game_settings(6, "one")
            return player
        elif difficulty == "H":
            tries = 8
            print("You chose Hard difficulty. You have ", tries, "tries")
            difficulty_selected = True
            player = game_settings(8, "two")
            return player
        elif difficulty == "VH":
            tries = 6
            print("You chose Very Hard difficulty. You have ", tries, "tries")
            difficulty_selected = True
            player = game_settings(6, "two")
            return player
        else:
            print(difficulty, "is not a difficulty")


def main():

    intro_logo()
    game_instance = select_difficulty()

    print(game_instance.lives, game_instance.hidden)
    play(game_instance)
    while (
       input("Play Again? Enter 'Y' for YES \n or any other letter for NO ").upper()
            == "Y"
    ):
        game_instance = select_difficulty()
        play(game_instance)


if __name__ == "__main__":
    main()
