import arcade

class Player():
    def __init__(self,x,y):
        self.center_x = x
        self.center_y = y
        self.speed = 4
        self.texture = arcade.make_soft_circle_texture(40,arcade.color.FOREST_GREEN)

    def display(self):
        pass

    def update(self,deltatime=None):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0

        if self.right > 1000:
            self.right = 1000

class FastEnemy():
    def __init__(self,x,y):
        self.center_x = x
        self.center_y = y
        self.texture = arcade.make_soft_square_texture(30,arcade.color.RED_DEVIL)

    def move(self,deltatime=None):
        self.center_x += self.change_x

        #bounce off the window walls
        if self.left < 0 or self.right > 1000:
            self.change_x *= -1