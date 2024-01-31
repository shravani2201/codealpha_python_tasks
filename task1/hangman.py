import random
import time

def choose_word():
    words = ["python", "hangman", "programming", "computer", "gaming", "openai"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def display_hangman(incorrect_attempts):
    hangman_drawing = [
        """
         -----
         |   |
         O   |
             |
             |
             |
        --------
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        --------
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        --------
        """,
        """
         -----
         |   |
         O   |
        /|\   |
             |
             |
        --------
        """,
        """
         -----
         |   |
         O   |
        /|\  |
         |   |
             |
        --------
        """,
        """
         -----
         |   |
         O   |
        /|\  |
         |   |
        /    |
        --------
        """,
        """
         -----
         |   |
         O   |
        /|\  |
         |   |
        / \  |
             |
        --------
        """
    ]
    return hangman_drawing[incorrect_attempts]

def hangman():
    print("Welcome to Hangman!")
    name = input("What is your name?")
    time.sleep(1)
    print("Let's start the game",name)
    max_attempts = 6
    while max_attempts>0:
        word_to_guess = choose_word()
        guessed_letters = []
        incorrect_attempts = 0
        print("\nNew round:")
        print(display_word(word_to_guess, guessed_letters))
        
        while incorrect_attempts < max_attempts:
            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a valid single letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
                continue

            guessed_letters.append(guess)

            if guess not in word_to_guess:
                incorrect_attempts += 1
                print("Incorrect guess! Attempts remaining:", max_attempts - 1)
                print(display_hangman(incorrect_attempts))
            else:
                print("Good guess!")

            current_display = display_word(word_to_guess, guessed_letters)
            print(current_display)

            if "_" not in current_display:
                print("Congratulations! You guessed the word:", word_to_guess)
                break

        if "_" in current_display:
            print("Sorry, you ran out of attempts. The correct word was:", word_to_guess)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'yes':
            continue
        else:
            break

if __name__ == '__main__':
    hangman()
