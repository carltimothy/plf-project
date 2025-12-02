import os
import sys

def Create():
    if (os.path.exists("user.txt") == False):
        file = open("user.txt", "x")
        file.close()
    if (os.path.exists("pass.txt") == False):
        file = open("pass.txt", "x")
        file.close()

def login():
    print("=== LOGIN ===")
    user = input("Enter username: ").strip()
    passw = input("Enter password: ").strip()

    users_file = open("user.txt", "r")
    users = [u.strip() for u in users_file.readlines()]
    users_file.close()

    pass_file = open("pass.txt", "r")
    passwords = [p.strip() for p in pass_file.readlines()]
    pass_file.close()

    if user in users:
        index = users.index(user)
        if index < len(passwords) and passwords[index] == passw:
            print("Login Successful!")
        else:
            print("Wrong password.")
    else:
        print("Username not found.")

def signup():
    print("=== USER REGISTRATION ===")
    username = input("Enter a username: ").strip()
    password = input("Enter a password: ").strip()
    file = open("user.txt", "a")
    file.write(username + "\n") 
    file.close()
    file = open("pass.txt", "a")
    file.write(password + "\n") 
    file.close()

def Main():
    signup()
    login()
    while True:
        print("\n [1] Re-register" \
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