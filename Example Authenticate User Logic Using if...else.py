# Username and password stored in database
username_db = "admin"
password_db = "sparrow@123"

# Username and password entered by the user
username = input("Enter username: ")
password = input("Enter password: ") 

# Check if username & password in database matches user's input
if (username == username_db) and (password == password_db):
    print("Welcome back.")
else:
    print("Access denied.")