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

        #creating objects of game characters
        self.hero = Player(name="WEWOW",x=200,y=100)
        self.enemy = FastEnemy(enemy_type="Goblin",x=800,y=100)

    def on_draw(self):
        #roughly takes 60 times in a second to redraw

        #self.clear is important to clear the screen after every frame
        self.clear()

        #draw our characters using simple placeholder shapes
        #drawing player as green circle
        arcade.draw_circle_filled(self.hero.x,self.hero.y,radius=20,color=arcade.color.FOREST_GREEN)

        #drawing enemy as red square
        arcade.draw_lbwh_rectangle_filled(self.enemy.x,self.enemy.y,30,30,arcade.color.RED)

        #drawing on screen text
        arcade.draw_text("This is first arcade game and game loop is running",20,500,arcade.color.SAND,17)

    def on_update(self, delta_time):
        self.enemy.move(delta_time)

#define a function to start the main engine
def startup():
    window = Arena_Engine()

    #starting lifecycle of looping engine
    arcade.run()

startup()        
