import os

def Creation():
    if (os.path.exists("list.txt") == False):
        file = open("list.txt", "x")
        file.write("|| LASTNAME || FIRSTNAME || PROGRAM || YEAR LEVEL|| \n")
        file.close()

def Append():
    last = input("Enter Lastname: ")
    first = input("Enter Firstname: ")
    program = input("Enter Program: ")
    year = input("Enter Year Level: ")
    file = open("list.txt", "a")
    file.write(f"|| {last} || {first} || {program} || {year} || \n")
    print("New Data Added.")
    file.close()

def Read():
    file = open("list.txt", "r")
    print(file.read())
    file.close()

def Remove():
    if os.path.exists("list.txt"):
        os.remove("list.txt")
        print("File 'list.txt' has been deleted.")
    else:
        print("File 'list.txt' does not exist.")

def Main():
    Creation()
    print("Created since file is missing.")
    while True:
        user = input("\n [1] Add Content. \n [2] Read File Content. \n [3] Delete File. \n [4] Exit Program.\n Choose an option: ")
        if user == '1':
            Append()
        elif user == '2':
            Read()
        elif user == '3':
            Remove()
        elif user == '4':
            break

Main()
