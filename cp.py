import os
import sys

def Create():
    if not os.path.exists("user.txt"):
        open("user.txt", "x").close()
    if not os.path.exists("pass.txt"):
        open("pass.txt", "x").close()

def login():
    print("=== LOGIN ===")
    input_user = input("Enter username: ").strip()
    input_pass = input("Enter password: ").strip()

    user_file = open("user.txt", "r")
    users = [u.strip() for u in user_file.readlines()]
    user_file.close()

    pass_file = open("pass.txt", "r")
    passwords = [p.strip() for p in pass_file.readlines()]
    pass_file.close()

    if input_user in users:
        index = users.index(input_user)
        if index < len(passwords) and passwords[index] == input_pass:
            print("Login successful!")
            return True
        else:
            print("Wrong password.")
            return False
    else:
        print("Username not found.")
        return False

def signup():
    print("=== REGISTRATION ===")
    username = input("Enter a username: ").strip()
    password = input("Enter a password: ").strip()
    with open("user.txt", "a") as f:
        f.write(username + "\n")
    with open("pass.txt", "a") as f:
        f.write(password + "\n")

def Main():
    Create()
    signup()
    if not login():
        print("Access denied. Exiting program.")
        sys.exit()

    while True:
        print("==== WELCOME TO THE SYSTEM ====")
        print("\n [1] Re-register"
              "\n [2] End Program")
        choice = input("Input: ")
        if choice == "1":
            signup()
        elif choice == "2":
            os.remove("user.txt")
            os.remove("pass.txt")
            sys.exit()
        else:
            print("Invalid choice — enter 1 or 2.")

Main()