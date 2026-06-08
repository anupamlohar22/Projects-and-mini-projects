# Import random module for password generation
import random

# Import string module for character sets
import string

# Create a list of common passwords that should not be allowed
common_passwords = ["123456", "password", "12345678", "qwerty", "admin"]

# Ask the user to enter a password
password = input("Enter your password: ")

# Check if the password is a common password
if password.lower() in common_passwords:
    # Display warning message
    print("This is a very common password. Please choose another one.")
else:

    # Create a list to store missing requirements
    missing = []

    # Check if password length is at least 8 characters
    has_length = len(password) >= 8

    # Check if password contains uppercase letters
    has_upper = any(char.isupper() for char in password)

    # Check if password contains lowercase letters
    has_lower = any(char.islower() for char in password)

    # Check if password contains numbers
    has_digit = any(char.isdigit() for char in password)

    # Check if password contains special characters
    has_special = any(not char.isalnum() for char in password)

    # Count how many requirements are satisfied
    score = 0

    # Add score for length requirement
    if has_length:
        score += 1
    else:
        missing.append("At least 8 characters")

    # Add score for uppercase requirement
    if has_upper:
        score += 1
    else:
        missing.append("Uppercase letter (A-Z)")

    # Add score for lowercase requirement
    if has_lower:
        score += 1
    else:
        missing.append("Lowercase letter (a-z)")

    # Add score for number requirement
    if has_digit:
        score += 1
    else:
        missing.append("Number (0-9)")

    # Add score for special character requirement
    if has_special:
        score += 1
    else:
        missing.append("Special character (@,#,$,%,&)")

    # Determine password strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    # Display password strength
    print("\nPassword Strength:", strength)

    # Display feedback based on strength
    if strength == "Weak":
        print("Your password is weak.")
        print("Suggestions to improve:")

        # Show all missing requirements
        for item in missing:
            print("-", item)

    elif strength == "Medium":
        print("Your password is medium strength.")
        print("Consider adding:")

        # Show missing requirements
        for item in missing:
            print("-", item)

    else:
        print("Your password is strong!")

    # Generate a strong password recommendation
    recommended_password = (
        random.choice(string.ascii_uppercase) +
        random.choice(string.ascii_lowercase) +
        random.choice(string.digits) +
        random.choice("@#$%&*!") +
        ''.join(random.choices(
            string.ascii_letters + string.digits + "@#$%&*!",
            k=8
        ))
    )

    # Display recommended password
    print("\nRecommended Strong Password:", recommended_password)