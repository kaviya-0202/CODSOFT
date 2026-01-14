import random
import string

print("PASSWORD GENERATOR")

# User input
length = int(input("Enter desired password length: "))

print("Choose password complexity:")
print("1. Letters only")
print("2. Letters and numbers")
print("3. Letters, numbers, and symbols")

choice = input("Enter choice (1/2/3): ")

# Define character sets
if choice == "1":
    characters = string.ascii_letters
elif choice == "2":
    characters = string.ascii_letters + string.digits
elif choice == "3":
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid choice")
    exit()

# Generate password
password = ""
for i in range(length):
    password += random.choice(characters)

# Display password
print("Generated Password:", password)
