import arcade
from enemies import Player, FastEnemy

#setting up global screen dimensions

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "CODE ARCADE ENGINE"

#Creating our main game class to inherit all window powers from arcade.Window

class Arena_Engine(arcade.Window):
    def __init__(self):
        pass