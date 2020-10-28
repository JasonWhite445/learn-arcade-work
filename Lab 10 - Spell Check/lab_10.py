import re

def split_line(line):

    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

def main():

    my_file = open("dictionary.txt")
    dictionary_list = []
    line_number = 0

    for line in my_file:
        line = line.strip()
        dictionary_list.append(line)

    my_file.close()


    
    print("There were", len(dictionary_list), "names in the file.")

    print(" --- Linear Search --- ")

    my_story = open("AliceInWonderLand200.txt")

    for line in my_story:
        word_list = split_line(line)
        line_number += 1
        for word in word_list:
            i = 0
            while i < len(dictionary_list) and dictionary_list[i] != word.upper():
                i+=1
            if i == len(dictionary_list):
                print("Line", line_number, " possible misspelled word:", word)

    my_story.close()

    print(" --- Binary Search --- ")


    line_number = 0

    binary_story = open("AliceInWonderLand200.txt")

    for line in binary_story:
        word_list = split_line(line)
        line_number += 1
        for word in word_list:
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False
            while lower_bound < upper_bound and not found:
                middle_pos = (lower_bound + upper_bound) // 2
                if dictionary_list[middle_pos] < word.upper():
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > word.upper():
                    upper_bound = middle_pos
                else:
                    found = True
            if not found:
                print("Line", line_number, " possible misspelled word:", word)


    binary_story.close()

main()
