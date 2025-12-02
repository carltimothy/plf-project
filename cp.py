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
    print("===LOGIN===")
    user = input("Enter username: ").strip()
    passw = input("Enter password: ").strip()
    user = open("user.txt", "r")
    users = (u.strip() for u in user.readlines())
    user.close()
    password = open("pass.txt", "r")
    passwords = (p.strip() for p in password.readlines())
    password.close()
    if user in users:
        index = users.index(user)
        if index < len(passwords) and passwords[index] == passw:
            print("")
        else:
            print("")
    else:
        print("")

def signup():
    print("===REGISTRATION===")
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
        print("====WELCOME TO THE SYSTEM===")
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