import random


# function that find the card area which user chooses
def find_area_num(x, y):
    if x in range(210, 290):
        if y in range(45, 165):
            return 1
        if y in range(175, 295):
            return 5
        if y in range(305, 425):
            return 9
        if y in range(435, 555):
            return 13
    if x in range(310, 390):
        if y in range(45, 165):
            return 2
        if y in range(175, 295):
            return 6
        if y in range(305, 425):
            return 10
        if y in range(435, 555):
            return 14
    if x in range(410, 490):
        if y in range(45, 165):
            return 3
        if y in range(175, 295):
            return 7
        if y in range(305, 425):
            return 11
        if y in range(435, 555):
            return 15
    if x in range(510, 590):
        if y in range(45, 165):
            return 4
        if y in range(175, 295):
            return 8
        if y in range(305, 425):
            return 12
        if y in range(435, 555):
            return 16


# function takes a list and returns an area number randomly
def random_area_num(card_list):
    temp_list = []
    temp_list = list(card_list)
    # shuffle the list every time
    random.shuffle(temp_list)
    for i in range(temp_list.__len__()):
        if not temp_list[i].shown:
            x = temp_list[i].card_area[0]
            y = temp_list[i].card_area[1]
            return find_area_num(x, y)

