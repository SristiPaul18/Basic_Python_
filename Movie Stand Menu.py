menu = {
    # Popcorn
    "Popcorn (Small)": 3.50,
    "Popcorn (Medium)": 5.00,
    "Popcorn (Large)": 6.50,
    "Caramel Popcorn": 4.25,
    "Cheese Popcorn": 4.75,

    # Drinks
    "Soft Drink (Small)": 2.00,
    "Soft Drink (Medium)": 3.00,
    "Soft Drink (Large)": 4.00,
    "Bottled Water": 2.00,
    "Iced Tea": 2.50,
    "Lemonade": 2.75,
    "Coffee": 2.25,
    "Hot Chocolate": 2.50,
    "Energy Drink": 3.50,

    # Hot Foods
    "Hot Dog": 3.75,
    "Chili Cheese Dog": 4.50,
    "Nachos with Cheese": 4.50,
    "Loaded Nachos": 5.50,
    "Pizza Slice": 3.00,
    "Chicken Tenders (3 pcs)": 4.75,
    "French Fries": 3.25,
    "Mozzarella Sticks": 4.25,

    # Candy
    "Gummy Bears": 2.50,
    "M&Ms": 2.75,
    "Skittles": 2.75,
    "Sour Patch Kids": 2.75,
    "Chocolate Bar": 2.50,
    "Reese's Cups": 2.75,

    # Desserts
    "Ice Cream Cup": 2.75,
    "Ice Cream Sandwich": 3.00,
    "Brownie": 2.50,
    "Churros": 3.00,
    "Milkshake": 3.75,

    # Combos
    "Popcorn + Drink Combo": 7.50,
    "Hot Dog + Drink Combo": 6.50,
    "Nachos + Drink Combo": 7.00
}

cart = []
total = 0

print("=" * 50)
print("             MOVIE THEATRE MENU              ")
print("=" * 50)

for key, value in menu.items():
    print(f"{key:<30} ${value:>5.2f}")
print("=" * 50)

while True:
    food = input("Select an item (or press q to quit):")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        print(f"'{food}' added to your cart.\n")
    else:
        print("Item not found in menu. Please try again.\n")

print("\n" + "-" * 50)
print("                    YOUR ORDER")
print("-" * 50)

for food in cart:
    price = menu.get(food)
    total += price
    print(f"{food:<30} ${price:>5.2f}")

print("-" * 50)
print(f"{'Total':<30} ${total:>5.2f}")
print("=" * 50)
print("         Thank you for your purchase!")
print("=" * 50)