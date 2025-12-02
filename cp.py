import os
import sys

def Create():
    if not os.path.exists("user.txt"):
        file = open("user.txt", "x")
        file.close()
    if not os.path.exists("pass.txt"):
        file = open("pass.txt", "x")
        file.close()

def login():
    print("=== LOGIN ===")
    user = input("Enter username: ").strip()
    passw = input("Enter password: ").strip()

    with open("user.txt", "r") as uf:
        users = [u.strip() for u in uf.readlines()]

    with open("pass.txt", "r") as pf:
        passes = [p.strip() for p in pf.readlines()]

    if user in users:
        index = users.index(user)
        if index < len(passes) and passes[index] == passw:
            print("Login successful!")
            return True

    print("Invalid username or password.")
    return False

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
            break
        else:
            print("Invalid choice — enter 1 or 2.")

Main()