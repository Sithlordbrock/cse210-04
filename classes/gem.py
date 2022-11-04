from classes.fallingitem import falling_item
from shared.color import Color

class Gem(falling_item):
    def __init__(self):
        """Gems"""
        super().__init__()
        self._text = "*"
        self.pointValue = 1
        self._color = Color(0,255,0)