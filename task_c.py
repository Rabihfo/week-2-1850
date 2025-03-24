# Ask user for a password
password = input("Enter a password: ").strip()

# Check password criteria
has_letter = any(char.isalpha() for char in password)
has_number = any(char.isdigit() for char in password)
is_long_enough = len(password) >= 8

# Validate password
if is_long_enough and has_letter and has_number:
    print("Your password is valid")
else:
    print("Your password must contain at least 8 characters, and a mix of letters and numbers")
