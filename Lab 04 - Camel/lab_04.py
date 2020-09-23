import math
import random

def main():
    #Instructions
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert")
    print("The natives want their camel back and are chasing you down!")
    print("Survive your desert trek and out run the natives.")
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    native_distance = -20
    canteens = 3

    done = False
    while not done:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status Check.")
        print("Q. Quit.")
        user_choice = input("What is your choice? ")
        if user_choice == "Q" or "q":
            done = True
            print("You have decided to quit... coward.")
        elif user_choice == "E" or "e":
            print("Miles traveled: " + miles_traveled)
            print("Drinks in canteen" + canteens)
            print("The natives are " + native_distance + " miles behind you!")
        elif user_choice == "D" or "d":
            print("Your camel is happy from a good nights rest")
            camel_tiredness = 0
            native_distance += random.random() * 7 + 7
            math.trunc(native_distance)
        elif user_choice == "C" or "c":
            miles_traveled += random.random() * 10 + 11
            math.trunc(miles_traveled)
            print("You have traveled " + miles_traveled)
            thirst += 1




main()
