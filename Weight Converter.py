print("="*40)
print("         WEIGHT CONVERTER         ")
print("="*40)

print("Available units:")
print("Kilograms (kgs)")
print("Pounds    (lbs)")
print("Grams     (g)")
print("Ounces    (oz)")
print("Stones    (st)")
print("-" * 40)

weight = float(input("Enter your weight: "))
from_unit = input("Current unit (kgs, lbs, g, oz, st): ")
to_unit = input("Convert to (kgs, lbs, g, oz, st): ")

print("-" * 40)

to_kg = {
    "kgs": 1,
    "lbs": 0.453592,
    "g": 0.001,
    "oz": 0.0283495,
    "st": 6.35029
}

from_kg = {
    "kgs": 1,
    "lbs": 2.20462,
    "g": 1000,
    "oz": 35.274,
    "st": 0.157473
}

if from_unit in to_kg and to_unit in from_kg:
    weight_in_kg = weight * to_kg[from_unit]
    converted_weight = weight_in_kg * from_kg[to_unit]
    print(f"{weight} {from_unit} is equal to {round(converted_weight, 2)} {to_unit}")
else:
    print("Invalid unit entered.")

print("="*40)
print("          Conversion Done          ")
print("="*40)
