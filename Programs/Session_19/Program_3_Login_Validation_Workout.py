"""
Session 19 - Program 3: Login Validation (Workout)

Check the username first, and only then the password.

Sample Output:
Enter username: admin
Enter password: 1234
Login Success

Try also: admin / wrong gives Invalid Password.
"""

# Program 3: Login validation (nested if)
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin":
    if password == "1234":
        print("Login Success")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")
