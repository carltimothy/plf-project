import os
import sys

def Main():
    stored_username = None
    stored_password = None
    if (os.path.exists("user.txt") == False):
        with open("user.txt", "x") as f:
            stored_username = f.read().strip().lower() or None
    if (os.path.exists("pass.txt") == False):
        with open("pass.txt", "x") as f:
            stored_password = f.read().strip() or None

    while True:
        print("What do you want to do?")
        print("\n 1. Create Account." \
              "\n 2. Login")
        choice = input("Input: ").strip()
        if choice == "1":
            stored_username, stored_password = signup()
        elif choice == "2":
            login(stored_username, stored_password)
        else:
            print("Invalid choice — enter 1 or 2.")

def signup():
    print("=== USER REGISTRATION ===")
    username = input("Enter a username: ").strip().lower()
    if not username.isalpha():
        print("Invalid username (letters only).")
        return None, None
    password = input("Enter a password: ").strip()
    if not password.isalnum():
        print("Invalid password (letters and numbers only).")
        return None, None

    try:
        with open("user.txt", "w", encoding="utf-8") as uf:
            uf.write(username + "\n")
        with open("pass.txt", "w", encoding="utf-8") as pf:
            pf.write(password + "\n")
    except OSError as e:
        print("Failed to save credentials:", e)
        return None, None

    print("Account created for", username)
    return username, password

def login(stored_username, stored_password):
    print("=== LOGIN ===")
    if not stored_username:
        print("No account registered. Choose 1 to create an account first.")
        return
    user = input("Enter username: ").strip().lower()
    if user != stored_username:
        print("Invalid Username!")
        return
    passw = input("Enter password: ").strip()
    if passw != stored_password:
        print("Invalid password!")
        return
    print("Login Successful!")
    print(f"Welcome, {stored_username}")
    print("Your password length is", len(stored_password), "characters.")
    print("*" * len(stored_password))
    sys.exit()

Main()
