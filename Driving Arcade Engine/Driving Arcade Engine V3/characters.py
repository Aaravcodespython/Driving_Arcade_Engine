import arcade

class Player(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.texture = arcade.load_texture(":resources:images/animated_characters/male_person/malePerson_idle.png")

    def update(self,deltatime=None):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0

        if self.right > 1000:
            self.right = 1000

class FastEnemy(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.speed = 3
        self.texture = arcade.make_soft_square_texture(30,arcade.color.RED_DEVIL)

    def update(self,deltatime=None):
        self.center_x += self.speed

        #bounce off the window walls
        if self.left < 0 or self.right > 1000:
            self.speed *= -1