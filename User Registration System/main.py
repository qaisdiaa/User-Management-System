users_data = {}
special_characters = ['!', '@', '#', '$', '&', '*', '?', '.']


def register():
    while True:
        x = input("Enter a username: ")
        if len(x) < 5:
            print("Invalid username. Must be at least 5 characters long. Try again.")
        elif " " in x or any(char in x for char in special_characters):
            print("Username cannot contain spaces or special characters. Try again.")
        else:
            while True:
                y = input("Enter a password: ")
                if len(y) >= 8 and any(char.isdigit for char in y) and any(char.isupper for char in y) and any(char.islower for char in y) and any(char in y for char in special_characters):
                    users_data[x] = y
                    print("Registration successful!")
                    print("Current users:", users_data)
                    return
                else:
                    print("Password is too weak. Try again.")

def login():
    while True:
        x2 = input("Enter your username: ")
        if x2 not in users_data:
            print("Invalid credentials. Try again.")
        else:
            while True:
                y2 = input("Enter your password: ")
                if y2 not in users_data[x2]:
                    print("Invalid credentials. Try again.")
                else:
                    print("Login successful! Welcome back,", x2)
                return


print("Welcome to the User Management System!")
print("1. Register")
print("2. Login")
print("3. Exit")

while True:
    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            register()
        elif choice == 2:
            login()
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Please enter a number between 1 and 3")
    except ValueError:
        print("Wrong input. Enter a number between 1 and 3")

