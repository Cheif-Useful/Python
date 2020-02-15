# # First Python Program

# print("Hello World")

# # ---------------Classes

# # str int float list tuple dict set

# # ---------------Taking Input

# myVariable = input("Enter Your Name ")

# # ---------------STRING

# myStr = "Python is Good Language"
# print(myStr[::-1])                      # Slicing

# # ---------------List == Array

# myList = ["chinga", 12, "HEllo"]
# print(type(myList))

# # ---------------DICTIONARY

# myDict = {"chinga":"pro", "tu":"noob"}
# print(type(myDict))
# print(myDict["chinga"])

# # ---------------Exercise 1------------

# myDict = {"a":1,"b":2,"cat":"dog"}
# key = input("Search : ")
# print(key,"means :",myDict[key])

# # ---------------TUPLE

# myTup = ("hey", 1, 2)
# print(type(myTup))
# # myTup[0] = "new"                                  # immutable
# print(myTup)

# # ---------------SET

# mySet = set()
# mySet.add(1)
# mySet.add(2)
# mySet.add(3)
# mySet.add(4)
# mySet2 = set()
# mySet2.add(4)
# mySet2.add(5)
# mySet2.add(6)
# mySet2.add(7)
# print(mySet.union(mySet2))
# print(mySet.intersection(mySet2))

# # ----------------if elif else

# age = int(input("Enter Your age :"))
# if age>18 and age<100:
#     print("You can Drive")
# elif age == 18:
#     print("Will Take a Test")
# elif age<7:
#     print("Can't Drive")

# # ----------------Exercise 2------------

# # 45*9 74*3 12*3

# sign = input("You Want to (+,-,*,/) :")
# check = {45*9:400, 74*3:400, 12*3:400}
# num1 = int(input("1st No. :"))
# num2 = int(input("2nd No. :"))
# checkStr = num1*num2
# if checkStr in check:
#     print(check[checkStr])
# elif sign == "+":
#     print("Your ans is : ", num1+num2)
# elif sign == "-":
#     print("Your ans is : ", num1-num2)
# elif sign == "*":
#     print("Your ans is : ", num1*num2)
# elif sign == "/":
#     print("Your ans is : ", num1/num2)
# else:
#     print("Wrong Sign")

# # ----------------for loop

# myList = [["chinga","pro"],["carry","Good"],["C++","First Language"],["Python","Very Good Language"],["Java","Not Learned"]]
# for myItems, char in myList:
#     print(myItems,"is",char)

# # ----------------while break and continue

# # ----------------Exercise 4--------------

# hiddenNum = 18
# flag = 0
# tries = 1
# while tries<=5:
#     print(tries,"Try")
#     yourNum = int(input("Guess the no. : "))
#     if yourNum < hiddenNum:
#         print("Your Number is Smaller than hidden\n")
#         tries = tries + 1
#         if tries <= 5:
#             continue
#         else:
#             break
#     elif yourNum > hiddenNum:
#         print("Your Number is Greater than hidden.\n")
#         tries = tries + 1
#         if tries <= 5:
#             continue
#         else:
#             break
#     else:
#         print("!!You Win!!")
#         flag = 1
#         break
# if flag == 0:
#     print("\n!!You Lose!!")

# # ----------------Operators

# # Arithmatic(power - **, flor - //, remainder - %), Logical(Boolean and or), Identity(is ,is not), Membership(in, not in), Bitwise(& |)

# # ----------------Short Hand if else

# # print("This") if condition: else print("This")

# # ----------------Defining Function

# def myFunction(a,b):
#     '''This Function returns Percentage out of 300'''   #Doc String
#     percentage = (a/b)*100
#     return percentage
# myPercentage = myFunction(int(input("Enter Your Marks out of 300 : ")),300)
# print("Your Percentage is : ",myPercentage, end="%\n")
# print(myFunction.__doc__)

# #----------------File IO Basics
"""
"r" - Open file for reading --default
"w" - Open filr for writing
"x" - create file if not exist
"a" - add more content to file
"t" - text mode --default
"b" - binary mode
"+" - reade and write
"""

# myPointer = open("File.txt")
# print(myPointer.read(25))
# print(myPointer.readline())
# print(myPointer.readlines())
# for myLine in myPointer:
#     print(myLine,end="")
# myPointer.close()

# myPointer = open("File.txt", "a")
# noOfCharacters = myPointer.write("\nAur main Pro Bhi HU.")
# print(noOfCharacters)
# myPointer.close()

# myPointer = open("File.txt","r+")
# myPointer.write("\n Yeh Nai line h")
# myPointer = open("File.txt")
# myPointer.close()

# myPointer = open("File.txt")
# print(myPointer.tell())                 #Tell The location of pointer
# print(myPointer.read())
# print(myPointer.seek(17))
# print(myPointer.read())

# --------------With block                 doesn't need to close the file

# with open("File.txt") as myPointer:
#     print(myPointer.readline())
#     print(myPointer.tell())

# --------------Exercise 3

# noOfRows = int(input("Enter No Of Rows : "))
# yourBool = int(input("Enter '1' or '0' : "))
# myBool = bool()
# if yourBool == 1:
#     myBool = True
# elif yourBool == 0:
#     myBool = False
# else:
#     print("Wrong Input!!")
# if myBool == True:
#     for flag in range(0,noOfRows):
#         print("*"*(noOfRows-flag))
# elif myBool == False:
#     for flag in range(1,noOfRows+1):
#         print("*"*flag)
# else:
#     print("!!WTF!!")

# --------------Global keyword and Variable

# globalVar = 10
# print(globalVar)
# def aFunc():
#     global globalVar               # can change global variable by using global keyword
#     globalVar = 20
#     print(globalVar)
# aFunc()

# -------------importing and Using Modules

# import random

# randomNumber = random.random()
# dice = random.randint(1,6)
# print("Your Dice Shows : ", dice)
# print(randomNumber)
# myList = ["Chinga", "krunker.io", "Counter strike", "CS:GO"]
# print(random.choice(myList))

# import webbrowser
# import random

# urlList = ['https://www.krunker.io', 'https://www.youtube.com', 'https://www.google.com', 'https://www.github.com', 'https://www.stackoverflow.com']
# getUrl = random.choice(urlList)
# webbrowser.open(getUrl)

# -------------Using f-String

# a = "Krunker"
# b = "CS:Go"

# print(f"{b} is better than {a} but {a} is also very Good Game")

# -------------Exercise 6

# import random

# userScore = 0
# compScore = 0
# gameList = ["Stone", "Paper", "Scissors"]

# for i in range(1, 11):
#     comp = random.choice(gameList)
#     user = input("Stone 's', Paper 'p', Scissors 'sc' : ")
#     if user == "s":
#         user = "Stone"
#     elif user == "p":
#         user = "Paper"
#     elif user == "sc":
#         user = "Scissors"
#     else:
#         print("Wrong Input")
#         continue
     
#     if comp == "Stone":
#         if user == "Scissors":
#             compScore += 1
#             print("Computer choose Stone.")
#             print("You Lose This Round.")
#         elif user == "Paper":
#             userScore += 1
#             print("Computer choose Stone.")
#             print("You Won This Round.")
#         else:
#             print("Computer choose Stone.")
#             print("!! Draw !!")
#     elif comp == "Scissors":
#         if user == "Paper":
#             compScore += 1
#             print("Computer choose Scissors.")
#             print("You Lose This Round.")
#         elif user == "Stone":
#             userScore += 1
#             print("Computer choose Scissors.")
#             print("You Won This Round.")
#         else:
#             print("Computer choose Scissors.")
#             print("!! Draw !!")
#     elif comp == "Paper":
#         if user == "Stone":
#             compScore += 1
#             print("Computer choose Paper.")
#             print("You Lose This Round.")
#         elif user == "Scissors":
#             userScore += 1
#             print("Computer choose Paper.")
#             print("You Won This Round.")
#         else:
#             print("Computer choose Paper.")
#             print("!! Draw !!")

# if userScore > compScore:
#     print(f"You Won {userScore} Rounds and Lose {compScore} Rounds and {10-(userScore+compScore)} are Draw.")
#     print("!!!!!You Won!!!!!")
# elif userScore < compScore:
#     print(f"You Won {userScore} Rounds and Lose {compScore} Rounds and {10-(userScore+compScore)} are Draw.")
#     print("!!You Lose!!")
# else:
#     print(f"You Won {userScore} Rounds and Lose {compScore} Rounds and {10-(userScore+compScore)} are Draw.")
#     print("!!!Draw!!!")

# ----------args and kwargs  args -> Tuple; kwargs -> Dict or mapping can be renamed

# def myFunc(nrm, *args, **kwargs):
#     print(f"This is a normal {nrm}")
#     print(type(args))
#     print(type(kwargs))
#     for items in args:
#         print(items)
    
#     for key, tVal in kwargs.items():
#         print(f"{key} and {tVal}")

# myList = ["0", "1", "2", "3", "4"]
# myDict = {"one":"1", "two":"2", "three":"3", "four":"4"}
# normal = "Yes i am"
# myFunc(normal, *myDict, **myDict)

# ---------time modules

# import time

# initalTime = time.time()

# for i in range(10):
#     time.sleep(0.5)
#     print(f"This is {i}")

# print(f"For loop runned in {time.time()-initalTime} seconds")
# print(time.asctime(time.localtime(time.time())))

# ---------Enumerate 

# li = ["a","b","bd","aoos"]
# for i, items in enumerate(li):
#     if i%3 == 0:
#         print(f"Use of enumerate {items}")

# ---------- __name__ is always main for same program.

# if __name__ == "__main__":
#     pass

# ----------Join Function

# li = ["a", "2", "4", "5", "6"]
# print(" anything ".join(li))

# ----------Map

# li = ["2","34","6","8","90"]
# li = list(map(int , li))                    # type casted to integer
# square = list(map(lambda x: x*x, li))       # use of lambda
# print(square)
# li = [1,2,34,56,7,9]
# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
# func = [cube, square]
# for i in range(len(li)):
#     print(list(map(lambda x: x(li[i]), func)))

# ---------- Filter

# li = [1,2,3,4,5,6,7,8,9]
# print(list(filter(lambda x: x%3 == 0, li)))

# ---------- Reduce

# from functools import reduce
# li = [1,2,4,9]
# print(reduce(lambda x,y: x+y, li))

# ---------- Exercise 7

# 10 min total
# 2 min water (0 2 4 6 8 10)
# 3 min Eyes (3 6 9)
# 5 min physical (5 10)

# import pyttsx3
# import time

# engine = pyttsx3.init('espeak')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[10].id)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# if __name__ == "__main__":
#     while True:
#         print(time.asctime(time.localtime(time.time())))
#         speak("Drink Water")
#         water = input("Drink Water : ")
#         water = water.lower()
#         if water == "done":
#             print("OK\n")
#             speak("OK")
#             break
#         else:
#             print("\nWrong Input\n")
#             continue
#     time.sleep(4)  #120 sec
#     while True:
#         print(time.asctime(time.localtime(time.time())))
#         speak("Drink Water")
#         water = input("Drink Water : ")
#         water = water.lower()
#         if water == "done":
#             print("OK\n")
#             speak("OK")
#             break
#         else:
#             print("\nWrong Input\n")
#             continue
#     time.sleep(2)       #60 sec
#     while True:
#         print(time.asctime(time.localtime(time.time())))
#         speak("Please Relax your Eyes")
#         eyes = input("Please Relax your Eyes : ")
#         eyes = eyes.lower()
#         if eyes == "done":
#             print("OK\n")
#             speak("OK")
#             break
#         else:
#             print("\nWrong Input\n")
#             continue
#     time.sleep(2)       # 60 sec
#     while True:
#         print(time.asctime(time.localtime(time.time())))
#         speak("Drink Water")
#         water = input("Drink Water : ")
#         water = water.lower()
#         if water == "done":
#             print("OK\n")
#             speak("OK")
#             break
#         else:
#             print("\nWrong Input\n")
#             continue
#     time.sleep(2)       #60 sec
#     while True:
#         print(time.asctime(time.localtime(time.time())))
#         speak("Do Some Physical Exercise")
#         physical = input("Do Some Physical Exercise : ")
#         physical = physical.lower()
#         if physical == "done":
#             print("OK\n")
#             speak("OK")
#             break
#         else:
#             print("\nWrong Input\n")
#             continue
#     time.sleep(2)  #60 sec
#     while True:
#         print(time.asctime(time.localtime(time.time())))
#         speak("Drink Water")
#         water = input("Drink Water : ")
#         water = water.lower()
#         if water == "done":
#             print("OK\n")
#             speak("OK")
#             break
#         else:
#             print("\nWrong Input\n")
#             continue
#     while True:
#         print(time.asctime(time.localtime(time.time())))
#         speak("Please Relax your Eyes")
#         eyes = input("Please Relax your Eyes : ")
#         eyes = eyes.lower()
#         if eyes == "done":
#             print("OK\n")
#             speak("OK")
#             break
#         else:
#             print("\nWrong Input\n")
#             continue
#     time.sleep(4)  #120 sec
#     while True:
#         print(time.asctime(time.localtime(time.time())))
#         speak("Drink Water")
#         water = input("Drink Water : ")
#         water = water.lower()
#         if water == "done":
#             print("OK\n")
#             speak("OK")
#             break
#         else:
#             print("\nWrong Input\n")
#             continue
#     time.sleep(2)       #60 sec
#     while True:
#         print(time.asctime(time.localtime(time.time())))
#         speak("Please Relax your Eyes")
#         eyes = input("Please Relax your Eyes : ")
#         eyes = eyes.lower()
#         if eyes == "done":
#             print("OK\n")
#             speak("OK")
#             break
#         else:
#             print("\nWrong Input\n")
#             continue
#     time.sleep(2)       #60 sec
#     while True:
#         print(time.asctime(time.localtime(time.time())))
#         speak("Do Some Physical Exercise")
#         physical = input("Do Some Physical Exercise : ")
#         physical = physical.lower()
#         if physical == "done":
#             print("OK\n")
#             speak("OK")
#             break
#         else:
#             print("\nWrong Input\n")
#             continue
#     while True:
#         print(time.asctime(time.localtime(time.time())))
#         speak("Drink Water")
#         water = input("Drink Water : ")
#         water = water.lower()
#         if water == "done":
#             print("OK\n")
#             speak("OK")
#             break
#         else:
#             print("\nWrong Input\n")
#             continue