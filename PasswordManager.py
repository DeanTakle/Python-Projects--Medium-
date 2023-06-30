# Password Manager

import getpass  # for password input and masking

Login_info = {  # dictionary to store login credentials
    "username": "",
    "password": ""
}

passwords = {  # dictionary to store passwords
    "website": ["username", "password"]
}


def register():  # used to create an account for the user
    print('Enter login credentials')
    username = input('Username: ')  # get username from user
    password = getpass.getpass('Password: ')  # get password from user
    if password > 10:
        print('Your password is Strong')
    elif password < 5 and password > 10:
        print('Your password is Medium')
    elif password > 1 and password < 5:
        print('Your Username is Weak')
    else:
        print('Your password is invalid')
    confirm_password = getpass.getpass(
        'Confirm Password: ')  # confirm password from user
    if password == confirm_password:  # check if password and confirm password are the same
        Login_info["username"] = username  # store username in dictionary
        Login_info["password"] = password  # store password in dictionary
        print('Registration Successful')
        return True
    else:  # if password and confirm password are not the same then registration fails
        print('Registration Failed')
        return False


def login():  # used to login to the account
    print("Enter your login credentials")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    # check if username and password are the same as the ones stored in the dictionary
    if username == Login_info["username"] and password == Login_info["password"]:
        print("Login Successful")
        return True
    else:
        # if username and password are not the same as the ones stored in the dictionary then login fails
        print("Login Failed")
        return False


def main():
    print("Welcome to Password Manager")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = int(input("Enter your choice: "))  # get choice from user
    if choice == 1:  # if choice is 1 then register
        register()
    elif choice == 2:  # if choice is 2 then login
        login()
    elif choice == 3:  # if choice is 3 then exit
        exit()
    else:
        # if choice is not 1, 2 or 3 then invalid choice
        print("Invalid choice")
        main()


def passwords():  # used to add, view and delete passwords
    print("1. Add Password")
    print("2. View Password")
    print("3. Delete Password")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_password()
    elif choice == 2:
        view_password()
    elif choice == 3:
        delete_password()
    elif choice == 4:
        exit()
    else:
        print("Invalid choice")
        passwords()


def add_password():  # used to add passwords
    print("Enter the website name")
    website = input("Website: ")  # get website name from user
    print("Enter the username")
    username = input("Username: ")  # get username from user
    print("Enter the password")
    password = getpass.getpass("Password: ")  # get password from user
    print("Confirm the password")
    confirm_password = getpass.getpass(
        "Confirm Password: ")  # confirm password from user
    if password == confirm_password:  # check if password and confirm password are the same
        # store website name, username and password in dictionary
        passwords[website] = [username, password]
        print("Password added successfully")
    else:
        print("Password and confirm password are not the same")
        add_password()


def view_password():  # used to view passwords
    print("Enter the website name")
    website = input("Website: ")  # get website name from user
    if website in passwords:
        # print username and password
        print("Username: ", passwords[website][0])
        print("Password: ", passwords[website][1])
    else:
        print("Website not found")
        view_password()


def delete_password():  # used to delete passwords
    print("Enter the website name")
    website = input("Website: ")  # get website name from user
    if website in passwords:
        # delete website name, username and password from dictionary
        del passwords[website]
        print("Password deleted successfully")
    else:
        print("Website not found")
        delete_password()


main()
passwords()
