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
 _______                       _
(_______)                     | |
 _       ___  ____   ___  ___ | | _____
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
            difficulty_selected = True
        elif difficulty == "VH":
            tries = 6
            print("You chose Very Hard difficulty. You have ", tries, "tries")
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
                print("Great Job!", guess, "is a correct letter!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [
                    i for i, letter in enumerate(word)
                    if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guesed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
        elif len(guess) != len(word):
            print("Your guess does not have the right amount of letters!")
        else:
                guessed = True
                word_completion = word

    else:
        print("Woops! Please enter a letter or word! :)")
        print(display_hangman(tries))
        print(word_completion)
        print(f"There are {len(word)} letters in this word!")
        print("\n")
    if guessed:
        print(text_colors.GREEN + """Congrats, you guessed the word!
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
""" + text_colors.White)
    else:
        print(
            "Sorry, you ran out of tries. The word was " + word +
            "/n Maybe next time!")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                text_colors.RED + """
                    --------
                    |      |
                    |      O
                    |     \|/
                    |      |
                    |     / \.
                    - 
                
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
                """ + text_colors.WHITE,
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


def main():
    word = get_word()
    play(word)
    while input("Play Again? Enter 'Y' for YES"
                "\n or any other letter for NO ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()