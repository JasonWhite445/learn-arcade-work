class Item():
    def __init__(self, room_number, description, name):
        self.room_number = room_number
        self.description = description
        self.name = name
class Room():
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

    room = Room("You are in a old Dining Room. There are rooms to the north, east, and northeast.", 3, 1, None, None, 4, None, None, None)
    room_list.append(room)
    room = Room("You are in the long Southern Hallway. There are rooms to the north, east, west, northeast, and northwest.", 4, 2, None, 0, 5, 3, None, None)
    room_list.append(room)
    room = Room("You are in a stain ridden Bedroom. There are rooms to the north, west, and northwest.", 5, None, None, 1, None, 4, None, None)
    room_list.append(room)
    room = Room("You are in rusted, wet Bathroom. There are rooms to the south, east, northeast, and southeast.", None, 4, 0, None, 6, None, 1, None)
    room_list.append(room)
    room = Room("You are in the short Northern Hallway. There are rooms to the north, east, south, west, southeast, and southwest.", 6, 5, 1, 3, None, None, 2, 0)
    room_list.append(room)
    room = Room("You are in the hot Fire Pit Lounge. There are rooms to the south, west, northwest, and southwest.", None, None, 2, 4, None, 6, None, 1)
    room_list.append(room)
    room = Room("You are outside in the aroma filled Garden. There are rooms to the south, southeast, and southwest.", None, None, 4, None, None, None, 5, 3)
    room_list.append(room)
    done = True

    item_list = []
    current_item = 0

    item = Item(0, "There is a dirty plate on the table.", 0)
    item_list.append(item)
    item = Item(1, "There is a wax candle on the floor.", 1)
    item_list.append(item)
    item = Item(2, "There is a muddy pillow sheet at the foot of the bed.", 2)
    item_list.append(item)
    item = Item(3, "There is a piece of shattered mirror in the tub.", 3)
    item_list.append(item)
    item = Item(4, "There is a dagger hanging from the wall to your left.", 4)
    item_list.append(item)
    item = Item(5, "There are hot coals at he foot of the fire.", 5)
    item_list.append(item)
    item = Item(6, "A blue lily is situated in the center of the garden.", 6)
    item_list.append(item)

    item_list.append(item)

    print("This is a game where you travel from room to room using North, South, East, West, Northeast, Northwest, Southeast, and Southwest.")
    print("If at any point you would like to be finished press the q key or type quit.")

    while done is True:
        print(room_list[current_room].description, item_list[current_item].description)
        print()
        direction = str(input("What direction would you like to go? "))
        if direction.lower() == "north" or direction.lower() == "n":
            next_room = room_list[current_room].north
            next_item = item_list[next_room].room_number
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room
                current_item = next_item

        if direction.lower() == "east" or direction.lower() == "e":
            next_room = room_list[current_room].east
            next_item = item_list[next_room].room_number
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room
                current_item = next_item

        if direction.lower() == "south" or direction.lower() == "s":
            next_room = room_list[current_room].south
            next_item = item_list[next_room].room_number
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room
                current_item = next_item

        if direction.lower() == "west" or direction.lower() == "w":
            next_room = room_list[current_room].west
            next_item = item_list[next_room].room_number
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room
                current_item = next_item

        if direction.lower() == "southwest" or direction.lower() == "sw":
            next_room = room_list[current_room].southwest
            next_item = item_list[next_room].room_number
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room
                current_item = next_item

        if direction.lower() == "southeast" or direction.lower() == "se":
            next_room = room_list[current_room].southeast
            next_item = item_list[next_room].room_number
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room
                current_item = next_item

        if direction.lower() == "northwest" or direction.lower() == "nw":
            next_room = room_list[current_room].northwest
            next_item = item_list[next_room].room_number
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room
                current_item = next_item

        if direction.lower() == "northeast" or direction.lower() == "ne":
            next_room = room_list[current_room].northeast
            next_item = item_list[next_room].room_number
            if next_room is None:
                print("You can't go that way!")
            else:
                current_room = next_room
                current_item = next_item

        if direction.lower() == "q" or direction.lower() == "quit":
            done = False
            print("Thanks for playing!")

main()