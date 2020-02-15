# Log In Sign Up system with DATABASE as txt file by ChiNgA

import os
import time

while True:
    os.system("cls")

    print("->Log In Sign Up")
    navigation = input()

    if navigation == "d" or navigation == "a":
        os.system("cls")
        print("Log In ->Sign Up")
        navigation = input()
        if navigation == "s":
            os.system("cls")
            setUsername = input("Set Username : ")
            setPassword = input("Set Password : ")
            if setUsername == "" or setPassword == "":
                print("Username and Password can't be empty.")
                time.sleep(0.8)
                continue
            else:
                with open("database.txt", "a") as filePointer:
                    filePointer.write(f"{setUsername}-{setPassword}-\n")
                os.system("cls")
                print("Sucessfully Signed Up.")
                time.sleep(0.8)
                continue
    elif navigation == "s":
        os.system("cls")
        username = input('Username : ')
        username = f"{username}-"
        password = input('Password : ')
        with open("database.txt") as filePointer:
            db = filePointer.readlines()
            for lines in db:
                if username in lines:
                    if password == lines.split("-")[1]:
                        os.system("cls")
                        print("Welcome! You are Logged In.")
                        # Further Code.
                        time.sleep(2)
                        exit()
                    else:
                        os.system("cls")
                        print("Wrong Password!")
                        time.sleep(0.8)
                        continue
    else:
        exit()