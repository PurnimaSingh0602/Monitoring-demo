# login_demo.py

def login(username, password):
    # Hardcoded credentials (BAD PRACTICE ❌)
    stored_username = "admin"
    stored_password = "Admin@123"  

    if username == stored_username and password == stored_password:
        print("Login Successful ✅")
    else:
        print("Invalid Credentials ❌")


# User input
user = input("Enter username: ")
pwd = input("Enter password: ")

login(user, pwd)
