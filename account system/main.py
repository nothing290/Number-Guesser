import json
import time

filepath = "D:\\projects\\account system\\users.json" ## stores filepath of the .json file

# functions
def menu():
    while True:
        print("CLI Account Management System\n Welcome, user, what would you like to do today (you can enter 'exit' at anytime to exit)?\n 1. register an account\n 2. login to an existing account\n 3. exit")
        while True:
            try:
                choice = int(input(" : "))
            except ValueError:
                print("INVALID INPUT!")
                continue
            break
        if choice == 1:
            choice = "reg"
            break
        elif choice == 2:
            choice = "login"
            break
        elif choice == 3:
            print("EXITTING...")
            exit()
        else:
            print("INVALID OPTION!\n Please choose either 1, 2 or 3")
    return choice

def reg():
    print("ACCOUNT CREATION")
    while True:
        username = str(input("Enter a username : "))
        if username == "exit":
            print("EXITTING...")
            exit()
        if username not in data["users"]:
            break
        else:
            print("USERNAME ALREADY EXISTS!")
    while True:
        strength = 0
        password = str(input("Enter a password : "))
        if password == "exit":
            print("EXITTING...")
            exit()
        if len(password) < 8:
            print("PASSWORD MUST BE ATLEAST 8 CHARACTERS LONG!\n password strength : 0")
            continue
        elif password.isdigit():
            print("PASSWORD MUST CONTAIN A LETTER!\n password strength : 2")
        elif password == password.lower():
            print("PASSWORD MUST CONTAIN ATLEAST ONE CAPITAL LETTER\n password strength : 4")
            continue
        else:
            print("password strength : 5")
        
        passcnfrm = str(input("Re-enter password to confirm : "))
        if password == passcnfrm:
            print(f"Password accepted!\n Welcome, {username}, your account has been sucessfully created!")
            break
        else: 
            print("PASSWORDS DO NOT MATCH!")
        
    data["users"][username] = {
        "password" : password,
        "attempts" : 0,
        "locked" : False
    }

    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def login():
    while True:
        while True:
            print("ACCOUNT LOGIN")
            username = str(input("Enter your username : "))
            if username == "exit":
                print("EXITTING...")
                exit()
            if username in data["users"]:
                if data["users"][username]["locked"] == True:
                    print("ACCOUNT LOCKED!")
                else:
                    break
            else:
                print("USERNAME DOES NOT EXIST!")
                continue
        while True:
            if data["users"][username]["attempts"] < 5:
                password = str(input("Enter your password : "))
                if password == "exit":
                    exit()
                if password == data["users"][username]["password"]:
                    print(f"Password correct! Welcome back {username}")
                    data["users"][username]["attempts"] = 0
                    break
                else:
                    print("INCORRECT PASSWORD!")
                    data["users"][username]["attempts"] += 1
            else:
                print("TOO MANY INCORRECT ATTEMPTS, ACCOUNT LOCKED!")
                data["users"][username]["locked"] = True
                break
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
        if data["users"][username]["locked"] != True:
            break
        else:
            while True:
                print("Would you like to try another account? (Y/N)")
                try:
                    YN = str(input(" : "))
                except ValueError:
                    print("Please enter only Y or N")
                if YN == "y" or YN == 'Y' or YN == 'n' or YN == 'N':
                    break
                else:
                    print("Please enter only Y or N")

        if YN == 'y' or YN == 'Y':
            time.sleep(1)
        else:
            break

# boot
print("BOOTING...")
try:
    with open(filepath, 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    data = {
        "users" : {

        }
    }
    print("ERROR OCCURED!")
    time.sleep(1)
    print("ERROR RESOLVED!")
time.sleep(2)
print("BOOTUP COMPLETE.")
time.sleep(1)

# main
while True:
    choice = menu()
    if choice == "reg":
        reg()
    elif choice == "login":
        login()
    else:
        print("UNKNOWN ERROR!")

    print("What would you like to do next?\n 1. logout\n 2. exit")
    while True:
        try:
            choice = int(input(" : "))
        except ValueError:
            print("INVALID INPUT!")
            continue
        break

    if choice == 1:
        print("LOGGING OUT...")
        time.sleep(1)
        print("SUCCESSFULLY LOGGED OUT!")
        time.sleep(0.5)
        continue
    elif choice == 2:
        print("EXITTING...")
    else:
        print("INVALID INPUT!")