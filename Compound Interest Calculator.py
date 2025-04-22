print("=" * 45)
print("         COMPOUND INTEREST CALCULATOR         ")
print("=" * 45)

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero")
    else:
        break

while True:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")
    else:
        break

total = principle * pow((1 + rate/100), time)

print("-" * 45)
print(f"Initial Amount     : ${principle:.2f}")
print(f"Annual Interest    : {rate:.2f}%")
print(f"Time Period        : {time} year(s)")
print("-" * 45)
print(f"Balance After {int(time)} Year(s): ${total:.2f}")
print("=" * 45)
print("             Calculation Complete              ")
print("=" * 45)