import string
import random

def generate_pass(min_length, use_numbers=True, use_special_chars=True):
    character = string.ascii_letters
    if use_numbers:
        character += string.digits
    if use_special_chars:
        character += string.punctuation
    
    pwd = []
    while len(pwd) < min_length:
        new_char = random.choice(character)
        pwd.append(new_char)

    # Ensure the generated password meets the specified criteria
    if use_numbers and not any(char.isdigit() for char in pwd):
        # If numbers are required but not present, add one
        pwd[random.randint(0, len(pwd) - 1)] = random.choice(string.digits)

    if use_special_chars and not any(char in string.punctuation for char in pwd):
        # If special characters are required but not present, add one
        pwd[random.randint(0, len(pwd) - 1)] = random.choice(string.punctuation)

    random.shuffle(pwd)
    return ''.join(pwd)

min_length = int(input("Length of the Password? "))
use_numbers = input("Do you want to use numbers in your password (Y/N)? ").lower() == "y"
use_special_chars = input("Do you want to use special characters in your password (Y/N)? ").lower() == "y"
password = generate_pass(min_length, use_numbers, use_special_chars)
print("Hey, congratulations on your new password: ", password)
