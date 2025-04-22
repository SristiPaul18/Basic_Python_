import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

print("=" * 60)
print("               MESSAGE ENCRYPTION SYSTEM")
print("=" * 60)

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text = cipher_text + key[index]

print("\n" + "-" * 60)
print("ENCRYPTION RESULT")
print("-" * 60)
print(f"Original Message : {plain_text}")
print(f"Encrypted Message: {cipher_text}")
print("-" * 60)

cipher_input = input("Enter a message to decrypt: ")
decrypted_text = ""

for letter in cipher_input:
    index = key.index(letter)
    decrypted_text += chars[index]

print("\n" + "-" * 60)
print("DECRYPTION RESULT")
print("-" * 60)
print(f"Encrypted Message: {cipher_input}")
print(f"Decrypted Message: {decrypted_text}")
print("=" * 60)

