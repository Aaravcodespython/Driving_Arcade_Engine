class Player():
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y
        self.speed = 4

    def display(self):
        pass

class FastEnemy():
    def __init__(self,enemy_type,x,y):
        self.enemy_type = enemy_type
        self.x = x
        self.y = y
        self.speed_x = -3

    def move(self,deltatime):
        #to find frame rate independence, multiply by deltatime
        #enemy moves with exact same speed on both slow or fast computer
        #60fps means roughly 0.016 seconds deltatime
        self.x += self.speed_x*deltatime*60

        #bounce off the window walls
        if self.x < 0 or self.x > 970:
            self.speed_x *= -1
