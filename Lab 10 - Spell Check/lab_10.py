class MnM:
    """ This is a class that represents an M&M. Don't modify it. """

    def __init__(self, color):
        """ Create an M&M with the specified color. """
        self.color = color
        self.flavor = "Chocolate"


def sort_out_green_candy(candy_list):
    # Write your code below this comment
    key = "Green"
    green_list = []
    for item in candy_list:
        if item.color == key:
            green_list.append(item)
    return green_list
    # Write your code above this comment


# These are some test cases
def test_1():
    candy_list = []
    candy_list.append(MnM("Green"))
    candy_list.append(MnM("Red"))
    candy_list.append(MnM("Blue"))
    candy_list.append(MnM("Brown"))
    candy_list.append(MnM("Green"))
    result = sort_out_green_candy(candy_list)
    print("Test 1, should be 2: ", len(result))


def test_2():
    candy_list = []
    candy_list.append(MnM("Green"))
    candy_list.append(MnM("Green"))
    candy_list.append(MnM("Brown"))
    candy_list.append(MnM("Green"))
    candy_list.append(MnM("Green"))
    result = sort_out_green_candy(candy_list)
    print("Test 2, should be 4: ", len(result))


test_1()
test_2()