from shared.color import Color
from shared.point import Point


class player():
    def __init__(self):
        """Constructs a new Player."""
        self.text = "#"
        self.color = Color(0,0,0)
        self.fontSize = 0
        self.position = Point(0,0)
        self.score = 0
        self.velocity = 0





    #setters
    def set_font_size(self, fontSize):
        self.fontSize = fontSize

    def set_velocity(self, velocity):
        self.velocity = velocity

    def set_position(self, postion):
        self.position = postion

    def set_color(self, color):
        self.color = color

    #getters
    def get_color(self):
        return self.color

    def get_text(self):
        return self.text

    def get_font_size(self):
        return self.fontSize

    def get_position(self):
        return self.position

    def get_velocity(self):
        return self.velocity


    def move_next(self, max_x, max_y):
        """Moves the player's to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_y (int): The maximum y value.
            max_x (int): The maximum x value.
        """
        y = (self.position.get_y() + self.velocity.get_y()) % max_y
        x = (self.position.get_x() + self.velocity.get_x()) % max_x
        self.position = Point(x,y)
