# Task 3: Password Generator
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def password_generator():
    try:
        length = int(input("Enter the length of the password: "))
        if length > 0:
            password = generate_password(length)
            print(f"Generated Password: {password}")
        else:
            print("Please enter a valid length.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    password_generator()


