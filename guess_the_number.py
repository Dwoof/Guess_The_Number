#!/usr/bin/env python

import random


def play_game(high):
    answer = random.randint(1, high)
    while True:
        try:
            guess = int(input("Guess the number between 1 and {:,}: \n".format(high)))
        except ValueError:
            print("Invalid Input... Please Use a Valid Integer.")
        else:
            break
    attempts = 1
    while answer != guess:
        attempts += 1
        if answer <= guess:
            while True:
                try:
                    guess = int(input("{:,} is too high... guess Lower!: ".format(guess)))
                except ValueError:
                    print("Invalid Input... Please Use a Valid Integer.")
                else:
                    break
        elif answer >= guess:
            while True:
                try:
                    guess = int(input("{:,} is too low... guess Higher!: ".format(guess)))
                except ValueError:
                    print("Invalid Input... Please Use a Valid Integer.")
                else:
                    break
    else:
        print("Correct - You Win!")
        print("You used: ", attempts, "attempts!")
        input("Press Enter to Return to Main Menu...")


print("Guessing Game... Choose Your Difficulty!\n----------------------------------------")
ans = True
while ans:
    print("""
    1. Easy: (1-100)
    2. Medium: (1-1,000)
    3. Hard: (1-10,000)
    4. Expert: (1-100,000)
    5. Insane: (1-1,000,000)
    6. Quit Game
    """)
    ans = input("Choose a difficulty: ")
    if ans == "1":
        play_game(100)
    elif ans == "2":
        play_game(1000)
    elif ans == "3":
        play_game(10000)
    elif ans == "4":
        play_game(100000)
    elif ans == "5":
        play_game(1000000)
    elif ans == "6":
        print("\n Exiting Game")
        ans = False
    elif ans == "7":
        print("***Secret Level Unlocked***")
        play_game(1000000000)
    else:
        print("\n Invalid Selection... Please Try Again:")


