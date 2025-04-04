import random
import string

def generate_password():
    print("Random Password Generator")
    length = int(input("Enter password length: "))
    
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("You must select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    print("Generated Password:", password)

generate_password()
