class Room():
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

def main():

    room_list = []
    current_room = 0

    room = Room("Dining Room", 3, 1, None, None)
    room_list.append(room)
    room = Room("South Hallway", 4, 2, None, 0)
    room_list.append(room)
    room = Room("Bedroom", 5, None, None, 1)
    room_list.append(room)
    room = Room("Bathroom", None, 4, 0, None)
    room_list.append(room)
    room = Room("North Hallway", 6, 5, 1, 3)
    room_list.append(room)
    room = Room("Fire pit lounge", None, None, 2, 4)
    room_list.append(room)
    room = Room("Garden", None, None, 4, None)
    room_list.append(room)
    done = True

    print("This is a game where you travel from room to room using North, South, East, and West.")
    print("If at any point you would like to be finished press the q key")

    while done is True:
        print("You are currently in the", room_list[current_room].description + ". There is a door to ")
        print()
        direction = str(input("What direction would you like to go? "))
        if direction.lower() == "north" or direction.lower() == "n":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room

        if direction.lower() == "east" or direction.lower() == "e":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room

        if direction.lower() == "south" or direction.lower() == "s":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room

        if direction.lower() == "west" or direction.lower() == "w":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room

        if direction.lower() == "q":
            done = False
            print("Thanks for playing!")

main()