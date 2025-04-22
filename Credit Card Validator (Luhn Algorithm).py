
sum_odd_digits = 0
sum_even_digits = 0
total = 0

print("=" * 60)
print("                CREDIT CARD VALIDATION")
print("=" * 60)

card_number = input("Enter a credit card number: ")
card_number = card_number.replace("-", "").replace(" ", "")

card_number = card_number[::-1]

for x in card_number[::2]:
    sum_odd_digits = sum_odd_digits + int(x)

for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits = sum_even_digits + (1 + ( x % 10))
    else:
        sum_even_digits = sum_even_digits + x

total = sum_even_digits + sum_odd_digits

print("\n" + "-" * 60)
print(f"Sum of odd-positioned digits : {sum_odd_digits}")
print(f"Sum of even-positioned digits: {sum_even_digits}")
print(f"Total checksum                : {total}")
print("-" * 60)

if total % 10 == 0:
    print("The card number is VALID.")
else:
    print("The card number is INVALID.")
print("=" * 60)