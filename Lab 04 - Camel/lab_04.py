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
        user_choice = str(input("What is your choice? "))
        if user_choice == "Q" or user_choice == "q":
            done = True
            print("You have decided to quit... coward.")
        elif user_choice == "E" or user_choice == "e":
            print("Miles traveled:",  miles_traveled)
            print("Drinks in canteen",  canteens)
            print("The natives are", miles_traveled - native_distance, "miles behind you!")
        elif user_choice == "D" or user_choice == "d":
            print("Your camel is happy from a good night's rest")
            camel_tiredness = 0
            native_distance += random.randrange(7, 15)
        elif user_choice == "C" or user_choice == "c":
            miles_traveled += random.randrange(10, 21)
            print("You have traveled",  miles_traveled,  "miles.")
            thirst += 1
            if random.randrange(0, 22) == 3:
                print("You have found an Oasis! Your water is refilled along with a rested camel.")
                camel_tiredness = 0
                canteens = 3
            camel_tiredness += random.randrange(1, 4)
            native_distance += random.randrange(7, 15)
        elif user_choice == "B" or user_choice == "b":
            miles_traveled += random.randrange(5, 12)
            math.trunc(miles_traveled)
            print("You have traveled",  miles_traveled,  "miles.")
            thirst += 1
            camel_tiredness += 1
            native_distance += random.randrange(7, 15)
        elif user_choice == "A" or user_choice == "a":
            if canteens > 0:
                canteens -= 1
                thirst = 0
            else:
                print("Error... you had no drinks left.")
        if not done and thirst > 6:
            done = True
            print("You have died of dehydration.")
        elif thirst > 4:
           done = True
           print("You are getting quite thirsty.")
        if camel_tiredness > 5 and camel_tiredness <= 8:
            print("Your camel is getting tired.")
        elif camel_tiredness > 8:
            done = True
            print("Your camel has died and as result so have you.")
        if native_distance >= miles_traveled:
            done = True
            print("The natives have caught you. Your death was not quick.")
        elif miles_traveled - native_distance <= 15:
            print("The natives are closing in!!!")
        if not done and miles_traveled >= 200:
            done = True
            print("You have survived the desert... good work.")


main()
