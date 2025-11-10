import random

ROCK = "r"
SCISSORS = "s"
PAPER = "p"
# to indent in python select all the code then press tab.
# Dictionaries are used to map a key -> value
emojis = {"r": "🪨", "s": "✂️", "p": "📄"}  # remember Windows key + full stop to open emoji keyboard
choices = tuple(emojis.keys())  # use a tuple this will help remove duplication fo code.


# to make sure the values must be read only because they must not be changed.
def get_user_choice():
    while True:
        user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()  # treating the user's text with lowercase
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice!")


def display_choices(user_choice, computer_choice):  # pass the values user_choice and computer choice to the functions
    print(f"You chose {emojis[user_choice]}")  # f is short for formatted
    print(f"Computer chose {emojis[computer_choice]}")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie!")
    elif (
            (user_choice == ROCK and computer_choice == SCISSORS) or
            (user_choice == SCISSORS and computer_choice == PAPER) or
            (user_choice == PAPER and computer_choice == ROCK)):
        print("You Win!")
    else:
        print("You lose")


def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)  # pass the values as arguments

        determine_winner(user_choice, computer_choice)

        should_continue = input("Continue? (y/n): ").lower()
        if should_continue == "n":
            break


# in order to use the code call the all the functions that were used.
play_game()
