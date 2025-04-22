import random

def spin_row():
    symbols = ['🍀', '💎', '🍒', '💰', '👑']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("\n[ " + " | ".join(row) + " ]\n")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 5
        elif row[0] == '💎':
            return bet * 15
        elif row[0] == '🍀':
            return bet * 10
        elif row[0] == '💰':
            return bet * 20
        elif row[0] == '👑':
            return bet * 50
    return 0

def main():
    balance = 100

    print("=" * 50)
    print("           WELCOME TO LUCKY LINE SLOT MACHINE")
    print("=" * 50)
    print("Match 3 of the same symbol to WIN! (10x payout)")
    print("Symbols: 🍀  💎  🍒  💰  👑")
    print("=" * 50)

    while balance > 0:
        print(f"Current balance is: ${balance}")
        bet = input("Enter your bet amount: $")

        if not bet.isdigit():
            print("Invalid input. Please enter a numeric value.")
            continue

        bet = int(bet)
        if bet > balance:
            print("Insufficient funds. Try a lower bet.")
            continue
        if bet <= 0:
            print("Bet must be greater than 0")
            continue
        balance = balance - bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"\nCongratulations! You won ${payout}")
        else:
            print("\nNo match. Better luck next time!")
        balance = balance + payout

        play_again = input("Would you like to spin again? (y/n): ").lower()
        if play_again != 'y':
            break

    print("\n" + "=" * 50)
    print(f"Game Over. Final Balance: ${balance:.2f}")
    print("Thank you for playing Lucky Line Slot Machine!")
    print("=" * 50)

if __name__ == '__main__':
    main()