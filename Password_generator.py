import random
import string


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError(
            "No character types selected, cannot generate password.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        use_upper = input(
            "Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_lower = input(
            "Include lowercase letters? (yes/no): ").lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

        password = generate_password(
            length, use_upper, use_lower, use_digits, use_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

