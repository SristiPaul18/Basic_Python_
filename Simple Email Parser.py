print("=" * 40)
print("             EMAIL PARSER              ")
print("=" * 40)

email = input("Enter your email address: ")

# Extract username and domain
username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print("-" * 40)
print(f"Email Address : {email}")
print(f"Username      : {username}")
print(f"Domain        : {domain}")
print("=" * 40)
print("           Parsing Complete            ")
print("=" * 40)
