def Addition(a, s):
    d = a + s
    print(d)
def Subtraction(a, s):
    d = a - s
    print(d)
def Mult(a, s):
    d = a * s
    print(d)
def Div(a, s):
    d = a / s
    print(d)
def Main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    choice = int(input("What would you like to do? \n"
                       "1. Addition \n"
                       "2. Subtraction \n"
                       "3. Multiplication \n"
                       "4. Division \n"))
    if choice == 1:
        Addition(num1, num2)
    elif choice == 2:
        Subtraction(num1, num2)
    elif choice == 3:
        Mult(num1, num2)
    elif choice == 4:
        Div(num1, num2)
    else:
        print("Not in choices")
Main()