print("=== REGISTRATION ===")
username = input("Enter a username: ").lower()
if not username.isalpha():
    print("Invalid username")
else:
    password = input("Enter a password: ").lower()
    if not password.isalnum():
        print("Invalid password")
    else:
        print("Account created successfully!")
        print("=== LOGIN ===")
        user = input("Enter username: ")
        if user != username:
            print("Invalid Username!")
        else:
            passw = input("Enter password: ")
            if passw != password:
                print("Invalid password!")
            else:
                print("Login Successful!")
                print(f"Welcome, {username}")
                print("Your password length is", len(password), "characters.")
                passw = "*" * len(password)
                print(passw)
