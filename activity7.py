import os
import sys

def Create():
    if not os.path.exists("user.txt"):
        open("user.txt", "x").close()
    if not os.path.exists("pass.txt"):
        open("pass.txt", "x").close()

def login():
    print("===LOGIN===")
    inp = input("Enter username: ").strip()
    inpp = input("Enter password: ").strip()
    user_file = open("user.txt", "r")
    pass_file = open("pass.txt", "r")
    if inp == user_file.readline().strip():
        pass_file.readline()
        if inpp == pass_file.readline().strip():
            print("Login Successful!")
        else:
            print("Wrong password.")
            sys.exit()
    else:
        print("Username not found.")
        sys.exit()
    user_file.close()
    pass_file.close()
    
def signup():
    print("===REGISTRATION===")
    username = input("Enter a username: ").strip()
    password = input("Enter a password: ").strip()
    with open("user.txt", "a") as f:
        f.write(username + "\n")
    with open("pass.txt", "a") as f:
        f.write(password + "\n")

def Main():
    Create()
    signup()
    login()
    while True:
        print("====WELCOME TO THE SYSTEM====")
        print("\n [1] Re-register"
              "\n [2] End Program")
        choice = input("Input: ")
        if choice == "1":
            signup()
        elif choice == "2":
            os.remove("user.txt")
            os.remove("pass.txt")
            sys.exit()

Main()
