import random
import string
import pyperclip

def generate_password(length=8, include_lowercase=True, include_uppercase=True, include_digits=True, include_symbols=True):
    # Define the character sets based on user-defined criteria
    lowercase_letters = string.ascii_lowercase if include_lowercase else ''
    uppercase_letters = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_digits else ''
    symbols = string.punctuation if include_symbols else ''

    # Combine the character sets into a single pool of characters
    characters = lowercase_letters + uppercase_letters + digits + symbols

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Get user input for password criteria
length = int(input("Enter the desired password length: "))
include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_digits = input("Include digits? (y/n): ").lower() == 'y'
include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

# Generate the password
password = generate_password(length, include_lowercase, include_uppercase, include_digits, include_symbols)
print("Generated Password:", password)

# Copy the password to the clipboard
pyperclip.copy(password)
print("Password copied to clipboard.")
