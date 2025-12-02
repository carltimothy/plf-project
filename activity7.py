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
    user = open("user.txt", "r")
    users = [u.strip() for u in user.readlines()]
    user.close()
    pass_file = open("pass.txt", "r")
    passwords = [p.strip() for p in pass_file.readlines()]
    pass_file.close()
    if inp in users:
        index = users.index(inp)
        if users.index(inp) < len(passwords) and passwords[index] == inpp:
            print("")
        else:
            print("")
            sys.exit()
    else:
        print("")
        sys.exit()

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
