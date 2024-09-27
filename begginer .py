import re

# Function to check the strength of a password
def check_password_strength(password):
    # Initialize score
    score = 0

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        print("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        print("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        print("Password should contain at least one lowercase letter.")

    # Check for digits
    if re.search(r"[0-9]", password):
        score += 1
    else:
        print("Password should contain at least one digit.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        print("Password should contain at least one special character.")

    # Final evaluation
    if score == 5:
        print("Strong password!")
    elif score >= 3:
        print("Moderate password.")
    else:
        print("Weak password. Consider making it stronger.")

    return score

# Main program
password = input("Enter a password to check its strength: ")
check_password_strength(password)