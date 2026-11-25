import random
import string
from collections import Counter


def guessing_game():

    score = 0
    best_score = 0

    while True:

        number = random.randint(1, 100)
        attempts = 5
        won = False

        print("\n--- Number Guessing Game ---")
        print("Guess the number between 1 and 100")

        while attempts > 0:

            try:
                guess = int(input("\nEnter your guess: "))

                if guess < 1 or guess > 100:
                    print("Enter number between 1 and 100")
                    continue

                attempts = attempts - 1

                if guess == number:
                    print("Correct! You guessed the number.")
                    won = True
                    score = 100 - ((5 - attempts - 1) * 10)
                    print("Your score:", score)
                    break

                elif guess < number:
                    print("Too low! Try again.")

                else:
                    print("Too high! Try again.")

                print("Attempts left:", attempts)

            except ValueError:
                print("Please enter a valid number.")

        if won == False:
            print("\nGame over!")
            print("The correct number was:", number)
            score = 0

        if score > best_score:
            best_score = score

        print("Best score:", best_score)

        play = input("\nDo you want to play again? (yes/no): ")

        if play.lower() != "yes":
            break


def word_counter():

    print("\n--- Word Counter ---")

    file_name = "sample.txt"

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            text = file.read()

        text = text.lower()
        text = text.translate(
            str.maketrans("", "", string.punctuation)
        )

        words = text.split()

        counts = Counter(words)

        print("\nTotal words:", len(words))
        print("Unique words:", len(counts))

        print("\nMost Common Words")
        print("----------------------")

        for word, count in counts.most_common(10):
            print(word, ":", count)

    except FileNotFoundError:
        print("Sample file not found!")


def main():

    while True:

        print("\n========================")
        print("       MAIN MENU")
        print("========================")
        print("1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            guessing_game()

        elif choice == "2":
            word_counter()

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Try again.")


main()