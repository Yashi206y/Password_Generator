import string
import random

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character set selected."
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input(prompt):
    return input(prompt).strip().lower() in ['yes', 'y']

def main():
    print("Password Generator")

    try:
        length = int(input("Enter password length:"))
        if length <= 0:
            print("Length must be greater than 0.")
            return
    except ValueError:
        print("Invalid number.")
        return
    
    use_upper = get_user_input("Include UPPERCASE letters? (yes/no): ")
    use_lower = get_user_input("Include lowercase letters? (yes/no): ")
    use_digits = get_user_input("Include numbers? (yes/no): ")
    use_symbols = get_user_input("Include symbols? (yes/no): ")

    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

    print("\nGenerated Password:")
    print(password)

if __name__ == "__main__":
    main()