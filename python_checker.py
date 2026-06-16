import re

def check_password(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1

    # Number check
    if re.search(r"\d", password):
        score += 1

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score == 5:
        print("Password Strength: Very Strong")
    elif score == 4:
        print("Password Strength: Strong")
    elif score == 3:
        print("Password Strength: Medium")
    elif score == 2:
        print("Password Strength: Weak")
    else:
        print("Password Strength: Very Weak")

    print("\nSuggestions:")
    if len(password) < 8:
        print("- Use at least 8 characters.")
        if not re.search(r"[A-Z]", password):
        print("- Add uppercase letters.")
    if not re.search(r"[a-z]", password):
        print("- Add lowercase letters.")
    if not re.search(r"\d", password):
        print("- Add numbers.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("- Add special characters.")

password = input("Enter Password: ")
check_password(password)
