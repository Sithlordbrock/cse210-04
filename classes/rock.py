from classes.fallingitem import falling_item
from shared.color import Color

class Rock(falling_item):
    def __init__(self):
        """Rocks"""
        super().__init__()
        self._text = "O"
        self.pointValue = -1
        self._color = Color(255,0,0)