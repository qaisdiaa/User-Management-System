                                                # User Management System

# Libraries
import os

# File to store user credentials
DATA_FILE = "users_data.txt"

special_characters = ['!', '@', '#', '$', '&', '*', '?', '.']

# Load users from file
def load_users():
    users = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                users[username] = password
    return users

# Save a new user to the file
def save_user(username, password):
    with open(DATA_FILE, "a") as file:
        file.write(f"{username},{password}\n")

# Validate and register a user
def register(users_data):
    while True:
        username = input("Enter a username: ")
        if len(username) < 5:
            print("Invalid username. Must be at least 5 characters long. Try again.")
        elif " " in username or any(char in username for char in special_characters):
            print("Username cannot contain spaces or special characters. Try again.")
        elif username in users_data:
            print("Username already exists. Try another one.")
        else:
            while True:
                password = input("Enter a password: ")
                if (
                    len(password) >= 8
                    and any(char.isdigit() for char in password)
                    and any(char.isupper() for char in password)
                    and any(char.islower() for char in password)
                    and any(char in password for char in special_characters)
                ):
                    users_data[username] = password
                    save_user(username, password)
                    print("Registration successful!")
                    return
                else:
                    print("Password is too weak. Try again.")

# Login functionality
def login(users_data):
    while True:
        username = input("Enter your username: ")
        if username not in users_data:
            print("Invalid credentials. Try again.")
        else:
            while True:
                password = input("Enter your password: ")
                if users_data[username] != password:
                    print("Invalid credentials. Try again.")
                else:
                    print(f"Login successful! Welcome back, {username}")
                    return

# Main program
def main():
    users_data = load_users()
    print("Welcome to the User Management System!")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                register(users_data)
            elif choice == 2:
                login(users_data)
            elif choice == 3:
                print("Goodbye!")
                break
            else:
                print("Please enter a number between 1 and 3")
        except ValueError:
            print("Wrong input. Enter a number between 1 and 3")

if __name__ == "__main__":
    main()

