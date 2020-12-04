"""
Text Adventure
"""
import random


class Item:
    def __init__(self, room_number, description, name):
        self.room_number = room_number
        self.description = description
        self.name = name


class Room:
    def __init__(self, description, north, east, south, west, northeast, northwest, southeast, southwest):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.northeast = northeast
        self.northwest = northwest
        self.southeast = southeast
        self.southwest = southwest


def main():

    room_list = []
    current_room = 0

    room = Room("You are in an old dining room.\nThere are rooms to the north, east, and northeast.",
                3, 1, None, None, 4, None, None, None)
    room_list.append(room)
    room = Room("You are in the long southern hallway. "
                "There are rooms to the north, east, west, northeast, and northwest.", 4, 2, None, 0, 5, 3, None, None)
    room_list.append(room)
    room = Room("You are in a stain ridden bedroom. There are rooms to the north, west, and northwest.", 5, None, None, 1, None, 4, None, None)
    room_list.append(room)
    room = Room("You are in rusted, wet bathroom. There are rooms to the south, east, northeast, and southeast.", None, 4, 0, None, 6, None, 1, None)
    room_list.append(room)
    room = Room("You are in the short northern hallway. "
                "There are rooms to the north, east, south, west, southeast, and southwest.", 6, 5, 1, 3, None, None, 2, 0)
    room_list.append(room)
    room = Room("You are in the hot fire pit lounge. "
                "There are rooms to the south, west, northwest, and southwest.", None, None, 2, 4, None, 6, None, 1)
    room_list.append(room)
    room = Room("You are outside in the aroma filled garden. "
                "There are rooms to the south, southeast, and southwest.", None, None, 4, None, None, None, 5, 3)
    room_list.append(room)
    done = True

    item_list = []

    item = Item(0, "There is a dirty plate on the table.", "plate")
    item_list.append(item)
    item = Item(1, "There is a wax candle on the floor.", "candle")
    item_list.append(item)
    item = Item(2, "There is a muddy pillow sheet at the foot of the bed.", "sheet")
    item_list.append(item)
    item = Item(3, "There is a piece of shattered mirror in the tub.", "mirror")
    item_list.append(item)
    item = Item(4, "There is a dagger hanging from the wall to your left.", "dagger")
    item_list.append(item)
    item = Item(5, "There are hot coals at he foot of the fire.", "coals")
    item_list.append(item)
    item = Item(6, "A blue lily is situated in the center of the garden.", "lily")
    item_list.append(item)

    health_points = 3
    monster_health_points = 5
    actions_performed = 0
    dagger_uses = 7

    print("This is a game where you travel from room to room "
          "using North, South, East, West, Northeast, Northwest, Southeast, and Southwest.")
    print("Try and slay what follows you. Something lurks in the dark... ")
    print("If at any point you would like to be finished press the q key or type quit.")

    while done is True:
        print(room_list[current_room].description)
        monster_room = random.randrange(7)
        chance_hit = random.randrange(2)
        actions_performed += 1
        # Print all the items in the current room
        for item in item_list:
            if current_room == item.room_number:
                print(item.description)
        print()

        # ask user for input
        user_input = input("What would you like to do? ")
        user_command = user_input.split(" ")

        # go a certain direction
        if user_input.lower() == "north" or user_input.lower() == "n":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room

        if user_input.lower() == "east" or user_input.lower() == "e":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room

        if user_input.lower() == "south" or user_input.lower() == "s":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room

        if user_input.lower() == "west" or user_input.lower() == "w":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room

        if user_input.lower() == "southwest" or user_input.lower() == "sw":
            next_room = room_list[current_room].southwest
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room

        if user_input.lower() == "southeast" or user_input.lower() == "se":
            next_room = room_list[current_room].southeast
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room

        if user_input.lower() == "northwest" or user_input.lower() == "nw":
            next_room = room_list[current_room].northwest
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room

        if user_input.lower() == "northeast" or user_input.lower() == "ne":
            next_room = room_list[current_room].northeast
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room

        # grab, drop, or use items
        if user_command[0].lower() == "get":
            success = False
            for item in item_list:
                if user_command[1].lower() == item.name and current_room == item.room_number:
                    item.room_number = -1
                    success = True
                    print(f"You have picked up a {item.name}.")
            if not success:
                print("That action cannot be performed.")

        if user_command[0].lower() == "drop":
            drop = False
            for item in item_list:
                if user_command[1].lower() == item.name and item.room_number == -1:
                    item.room_number = current_room
                    drop = True
                    print(f"You have dropped your {item.name}.")
            if not drop:
                print("That action cannot be performed.")

        if user_command[0].lower() == "show":
            full = False
            for item in item_list:
                if user_command[1].lower() == "inventory" and item.room_number == -1:
                    full = True
                    print(f"You have a {item.name} in your inventory.")
            if not full:
                print("That action cannot be performed.")

        if user_command[0].lower() == "use":
            equipped = False
            for item in item_list:
                if user_command[1].lower() == "dagger" and item.room_number == -1 and item.name == "dagger" and dagger_uses > 0:
                    equipped = True
                    print("You have slashed with your dagger! Your blade dulls.")
                    dagger_uses -= 1
            if not equipped:
                print("That action cannot be performed.")

        if user_command[0].lower() == "smell":
            picked = False
            for item in item_list:
                if user_command[1].lower() == "lily" and item.room_number == -1 and item.name == "lily":
                    picked = True
                    print(f"You take a long whiff of your beautiful flower...")
            if not picked:
                print("That action cannot be performed.")

        if monster_room == current_room:
            monster_input = input("Something moves toward you in the dark... What will you do? ")
            monster_command = monster_input.split(" ")
            if monster_command[0].lower() == "slash":
                attack = False
                for item in item_list:
                    if monster_command[1].lower() == "dagger" and item.room_number == -1 and item.name == "dagger":
                        dagger_uses -= 1
                        attack = True
                        if chance_hit == 0:
                            print("You have punctured the monster! It is retreating! Your dagger has dulled.")
                            monster_health_points -= 1
                        else:
                            print("The monster connects with a hit... Your wound will not heal. "
                                  "Your dagger has also dulled.")
                            health_points -= 1
                if not attack:
                    print("Unequipped, you are dealt a significant blow.")
                    health_points -= 1

        if monster_health_points == 0:
            done = False
            print("You have slayed the beast! A feat that any human would be proud of!")
            print("You performed", actions_performed, "actions.")

        if health_points == 0:
            done = False
            print("You have died by the monster. Game over!")
            print("You performed", actions_performed, "actions.")

        if user_input.lower() == "q" or user_input.lower() == "quit":
            done = False
            print("Thanks for playing!")


main()
