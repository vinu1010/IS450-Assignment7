import random

MAX_TRIES = 5
LOW, HIGH = 1, 20


def get_guess():
    """ask player for guess and keep asking until valid."""
    while True:
        text = input(f"Enter a guess ({LOW}-{HIGH}): ")
        if text.isdigit() and LOW <= int(text) <= HIGH:
            return int(text)
        print(f"Please enter a whole number from {LOW} to {HIGH}.")


def play_game():
    secret = random.randint(LOW, HIGH)
    guesses = []  # list of every guess made
    won = False

    print(f"I'm thinking of a number between {LOW} and {HIGH}.")
    print(f"You have {MAX_TRIES} tries.\n")

    while len(guesses) < MAX_TRIES:
        guess = get_guess()
        guesses.append(guess)

        if guess == secret:
            won = True
            break
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")
        print(f"Tries left: {MAX_TRIES - len(guesses)}\n")

    if won:
        print(f"\nYou got it! The number was {secret}.")
    else:
        print(f"\nOut of tries. The number was {secret}.")

    print(f"Your guesses: {guesses}")
    print(f"Total tries used: {len(guesses)}")


def main():
    print("=== Number Guessing Game ===")
    play_game()


main()