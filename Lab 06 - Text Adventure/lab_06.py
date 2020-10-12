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

    room = Room("You are in a old Dining Room. There are rooms to the north and east.", 3, 1, None, None)
    room_list.append(room)
    room = Room("You are in the long Southern Hallway. There are rooms to the north, east, and west.", 4, 2, None, 0)
    room_list.append(room)
    room = Room("You are in a stain ridden Bedroom. There are rooms to the north and west.", 5, None, None, 1)
    room_list.append(room)
    room = Room("You are in rusted, wet Bathroom. There are rooms to the south and east.", None, 4, 0, None)
    room_list.append(room)
    room = Room("You are in the short Northern Hallway. There are rooms in each direction.", 6, 5, 1, 3)
    room_list.append(room)
    room = Room("You are in the hot Fire Pit Lounge. There are rooms to the south and west.", None, None, 2, 4)
    room_list.append(room)
    room = Room("You are outside in the aroma filled Garden. Turn back to go back in the house.", None, None, 4, None)
    room_list.append(room)
    done = True

    print("This is a game where you travel from room to room using North, South, East, and West.")
    print("If at any point you would like to be finished press the q key or type quit.")

    while done is True:
        print(room_list[current_room].description)
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

        if direction.lower() == "q" or direction.lower() == "quit":
            done = False
            print("Thanks for playing!")

main()