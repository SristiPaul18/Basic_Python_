print("=" * 45)
print("             SHOPPING CART             ")
print("=" * 45)

foods = []
prices = []
total = 0.0

while True:
    food_item = input("Enter a food item to buy (or press q to quit): ")
    if food_item.lower() == "q":
        break

    price = float(input(f"Enter the price of '{food_item}': $"))
    foods.append(food_item)
    prices.append(price)
    total += price

print("\nFinal Receipt")
print("-" * 45)
print(f"{'No.':<5}{'Item':<25}{'Price':>5}")
print("-" * 45)

for i in range(len(foods)):
    print(f"{i + 1:<5}{foods[i]:<25}${prices[i]:>6.2f}")

print("-" * 45)
print(f"{'Total':<30}${total:>6.2f}")
print("=" * 45)
print("        Thank you for shopping!        ")
print("=" * 45)
