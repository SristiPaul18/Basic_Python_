def show_balance(balance):
    print("\n" + "-" * 45)
    print(f"Current Balance: ${balance:.2f}")
    print("-" * 45)

def deposit():
    amount = float(input("Enter amount to deposit: $"))

    if amount < 0:
        print("Invalid amount. Please enter a positive value.")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than zero.")
        return 0
    else:
        return amount

def show_transactions(transactions):
    print("\n" + "-" * 45)
    print("Transaction History")
    print("-" * 45)
    if not transactions:
        print("No transactions yet.")
    else:
        for t in transactions:
            print(t)
    print("-" * 45)

def main():
    balance = 0
    history = []
    is_running = True

    print("=" * 45)
    print("           WELCOME TO PYTHON BANK")
    print("=" * 45)

    while is_running:
        print("\nPlease choose an option:")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            amount = deposit()
            if amount > 0:
                balance += amount
                history.append(f"Deposited: ${amount:.2f}")

        elif choice == "3":
            amount = withdraw(balance)
            if amount > 0:
                balance -= amount
                history.append(f"Withdrew: ${amount:.2f}")

        elif choice == "4":
            print("\nTransaction History:")
            if not history:
                print("No transactions yet.")
            else:
                for h in history:
                    print("-", h)

        elif choice == "5":
            print("\nThank you for using Python Bank.")
            is_running = False
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")

if __name__ == '__main__' :
    main()