import random

lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number, highest_number)
guesses = 0
is_running = True

print("=" * 45)
print("         NUMBER GUESSING GAME")
print("=" * 45)
print(f"Guess the number between {lowest_number} and {highest_number}")
print()

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses = guesses + 1

        if guess < lowest_number or guess > highest_number:
            print(f"Out of range. Please select a number between {lowest_number} and {highest_number}.")
        elif guess < answer:
            print("Too Low. Try again.")
        elif guess > answer:
            print("Too High. Try again.")
        else:
            print("\n" + "-" * 45)
            print(f"Correct! The answer was {answer}.")
            print(f"Total guesses: {guesses}")
            print("Well done!")
            print("-" * 45)
            break
    else:
        print(f"Invalid input. Please enter a number between {lowest_number} and {highest_number}.")