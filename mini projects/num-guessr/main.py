# Quick introduction, this is only a little program i made to test GIT and GITHUB. i am currently learning python so there may be some mistakes and maybe this couldve been done in a better way. Either way, thanks for taking your time to check my work :)

import random as rn

filepath = r"highscore.txt"

num = rn.randint(1, 100)
guess = 0
attempts = 0

print("Hello user, this is a simple number guessing game.\n A number has been randomly selected and you will have to guess it until you're correct.\n The program will repeat until you guess correct or enter -1.\n Good Luck :)")

while guess != num:
    while True:
        try:
            guess = int(input("Enter a number between 1 and 100 : "))
        except:
            print("Error! Invalid input")
            continue

        if guess == -1:
            print(f"Alright, exitting. P.S; the number was {num}")
            break

        if guess > 0 and guess < 101:
            break
        else:
            print("Number is out of range")

    if guess == -1:
            break

    if attempts > 20:
        print(f"Sorry, you took too many attemps. The number was {num}")
        break

    if guess > num + 20:
        print("WAY TOO HIGH!")
        attempts += 1
    elif guess < num - 20:
        print("WAY TOO LOW!")
        attempts += 1
    elif guess > num:
        print("Too high")
        attempts += 1
    elif guess < num:
        print("Too low")
        attempts += 1
    else:
        attempts += 1
        print(f"Correct. you got it in {attempts}attempts!")

try:
    with open(filepath, 'r') as file:
        file.read()
except FileNotFoundError:
    with open(filepath, 'w') as file:
        file.write("1")

with open(filepath, 'r') as file:
    try:
        highscore = file.read().strip()
        if highscore:
            highscore = int(highscore)
        else:
            highscore = 0
    except:
        highscore = 1

print(f"Current highscore : {highscore}")
if highscore > attempts:
    print(f"You have the new highscore with {attempts} attempts")
    with open(filepath, 'w') as file:
        file.write(str(attempts))
else:
    print(f"Your score is {attempts}")