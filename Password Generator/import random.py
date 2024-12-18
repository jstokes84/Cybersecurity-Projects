import random
import string


def generate_password(length=12):
    #define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


if __name__ == "__main__":
    password_length = int(input("Enter the desired password length:"))

    if password_length < 1:
        print("Password length must be atleast 1 character.")
    else:
        generated_password = generate_password(password_length)
        print("generated password", generated_password)