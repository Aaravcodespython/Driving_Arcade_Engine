import arcade
from characters import Player, FastEnemy

#setting up global screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "CODE ARCADE ENGINE"

#Creating our main game class to inherit all window powers from arcade.Window
class Arena_Engine(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)

        #setting a solid background colour
        arcade.set_background_color(arcade.color.DARK_BLUE)

        #creating sprite list container for the player
        self.player_list = arcade.SpriteList()

        #creating objects of game characters
        self.hero = Player(x=200,y=100)
        
        self.player_list.append(self.hero)

        #creating sprite list container for the enemies
        self.enemies_list = arcade.SpriteList()
        self.enemies_list.append(FastEnemy(x=100,y=400))
        self.enemies_list.append(FastEnemy(x=600,y=450))
        self.enemies_list.append(FastEnemy(x=900,y=500))


    def on_draw(self):
        #roughly takes 60 times in a second to redraw

        #self.clear is important to clear the screen after every frame
        self.clear()

        #drawing player list
        self.player_list.draw()

        #drawing enemy list
        self.enemy_list.draw()

        #drawing on screen text
        arcade.draw_text("This is first arcade game and game loop is running",20,500,arcade.color.SAND,17)

    def on_update(self):
        self.player_list.update()
        self.enemies_list.update()

#define a function to start the main engine
def startup():
    window = Arena_Engine()

    #starting lifecycle of looping engine
    arcade.run()

startup()        