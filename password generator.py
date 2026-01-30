import random
import string


def generate_password(min_length, number=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation

    characters = letters
    if number:
        characters += digits
    if special_characters:
        characters += special_characters

    pwd = ""
    meets_criteria = False
    number = False
    has_special_characters = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            number = True
        elif new_char in special_characters:
            has_special_characters = True

        meets_criteria = True
        if number:
            number = True
        elif special_characters:
            has_special_characters = meets_criteria and has_special_characters



    return pwd
has_min_length = int(input("Input the minimum length of your password: "))
has_number = input("Do you want to have numbers(y/n)? ").lower() == "y"
has_special_characters = input("Do you want to have special characters(y/n)? ").lower() == "y"

pwd = generate_password(has_min_length, has_number, has_special_characters)

print(pwd)

choice = input("Do you do still want to generate a new password (y/n)? ").lower()
while choice == "y":
    pwd = generate_password(has_min_length, has_number, has_special_characters)
    print(pwd)
    choice = input("Do you do still want to generate a new password (y/n)? ").lower()
if choice == "n":
    print("Thank you for using the password generator!")