print("=" * 40)
print("         TEMPERATURE CONVERTER         ")
print("=" * 40)

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
temp = float(input("Enter the temperature: "))

print("-" * 40)

if unit == "C":
    converted = round(( 9 * temp ) / 5 + 32, 1)
    print(f"{temp}°C is equal to {converted}°F")
elif unit == "F":
    converted = round(( temp - 32 ) / 5 / 9, 1)
    print(f"{temp}°F is equal to {converted}°C")
else:
    print(f"'{unit}' is not a valid unit. Please enter 'C' or 'F'.")

print("=" * 40)
print("           Conversion Complete          ")
print("=" * 40)