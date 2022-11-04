from random import random
from shared.color import Color
from shared.point import Point

class falling_item():
    def __init__(self):
        """All Falling items start at the top of the
         screen and decend down the screen"""
        self._text = ""
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self.pointValue = 0

    def getPointValue(self):
        return self.pointValue

    def get_color(self):
        """Gets the item's color as a tuple of three ints (r, g, b).
        
        Returns:
            Color: The item's text color.
        """
        return self._color

    def get_font_size(self):
        """Gets the item's font size.
        
        Returns:
            Point: The item's font size.
        """
        return self._font_size

    def get_position(self):
        """Gets the item's position in 2d space.
        
        Returns:
            Point: The item's position in 2d space.
        """
        return self._position
    
    def get_text(self):
        """Gets the item's textual representation.
        
        Returns:
            string: The item's textual representation.
        """
        return self._text

    def get_velocity(self):
        """Gets the item's speed and direction.
        
        Returns:
            Point: The item's speed and direction.
        """
        return self._velocity
    
    def move_next(self, max_y):
        """Moves the item's to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_y (int): The maximum y value.
        """
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(y)

    def item_falling(self):
        y = (self._position.get_y() - 1)
        self._position = Point(y)

    def set_color(self, color):
        """Updates the color to the given one.
        
        Args:
            color (Color): The given color.
        """
        self._color = color

    def set_position(self, position):
        """Updates the position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position
    
    def set_font_size(self, font_size):
        """Updates the font size to the given one.
        
        Args:
            font_size (int): The given font size.
        """
        self._font_size = font_size
    
    def set_text(self, text):
        """Updates the text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.
        
        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity


