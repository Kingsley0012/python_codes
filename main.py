# python
import random
import string

def generate_password(min_length, use_numbers=True, use_special=True):
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation

    characters = letters
    if use_numbers:
        characters += digits
    if use_special:
        characters += specials

    pwd_chars = []
    has_number = False
    has_special = False

    while True:
        new_char = random.choice(characters)
        pwd_chars.append(new_char)

        if new_char in digits:
            has_number = True
        elif new_char in specials:
            has_special = True

        if len(pwd_chars) >= min_length:
            if (not use_numbers or has_number) and (not use_special or has_special):
                break

    return "".join(pwd_chars)

if __name__ == "__main__":
    min_len = int(input("Input the minimum length of your password: "))
    want_numbers = input("Do you want to have numbers(y/n)? ").strip().lower() == "y"
    want_specials = input("Do you want to have special characters(y/n)? ").strip().lower() == "y"

    pwd = generate_password(min_len, want_numbers, want_specials)
    print(pwd)

    while input("Do you still want to generate a new password (y/n)? ").strip().lower() == "y":
        pwd = generate_password(min_len, want_numbers, want_specials)
        print(pwd)

    print("Thank you for using the password generator!")
