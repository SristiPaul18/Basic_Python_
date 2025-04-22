import random

options = ("rock", "paper", "scissors")
running = True

print("=" * 50)
print("            ROCK, PAPER, SCISSORS GAME")
print("=" * 50)

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("\nEnter your choice (rock, paper, scissors): ").lower().strip()

    print("\n" + "-" * 50)
    print(f"Player    : {player}")
    print(f"Computer  : {computer}")
    print("-" * 50)

    if player == computer:
        print("Result    : It's a tie.")
    elif player == "rock" and computer == "scissors":
        print("Result    : You win! Rock crushes scissors.")
    elif player == "paper" and computer == "rock":
        print("Result    : You win! Paper covers rock.")
    elif player == "scissors" and computer == "paper":
        print("Result    : You win! Scissors cuts paper.")
    else:
        print(f"Result    : You lose! {computer} beats {player}.")

    print("-" * 50)
    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
        running = False

print("\nThank you for playing. Goodbye!")
print("=" * 50)