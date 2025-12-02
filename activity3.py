import os

def Read():
    file = open("list.txt", "r")
    print(file.read())
    file.close()

def Creation():
    if (os.path.exists("list.txt") == False):
        file = open("list.txt", "x")
        file.close()

def Append(fruit):
    file = open("list.txt", "a")
    file.write(fruit + "\n")
    file.close()

def Main():
    Creation()
    while True:
        fruit = input("What fruit to add? ")
        Append(fruit)   
        print("Fruits:")
        Read()
Main()
