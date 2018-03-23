import os

# global instances
width = 800
height = 600
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
dark_yellow = (200, 200, 0)
red = (255, 0, 0)
dark_red = (200, 0, 0)
green = (130, 255, 0)
dark_green = (100, 200, 0)
# coordinate for each card area
area_list = [(210, 45), (310, 45), (410, 45), (510, 45),
             (210, 175), (310, 175), (410, 175), (510, 175),
             (210, 305), (310, 305), (410, 305), (510, 305),
             (210, 435), (310, 435), (410, 435), (510, 435)]
# load game folder path
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
sound_folder = os.path.join(game_folder, "sound")
# will be used to define card position
value_in_area = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]
