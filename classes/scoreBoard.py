from shared.point import Point
from shared.color import Color
class scoreBoard():
    def __init__(self):
        # create the banner
        self.scoreBoardName = "Score"
        self.score = 0
        self.fontSize = 15
        self.color = Color(255, 255, 255)
        self.position = Point(15,1)
        
    def setScore(self, absoluteValue):
        self.score += absoluteValue
        
    def set_font_size(self, fontSize):
        self.fontSize = fontSize

    def setColor(self, color):
        self.color = color

    def setPosition(self, position):
        self.position = position
    
    #sets scoreboard name
    def set_text(self, text):
        self.scoreBoardName = text


    def getScoreBoardName(self):
        return self.scoreBoardName


    def getScore(self):
        return self.score

    def get_position(self):
        return self.position
    
    def get_font_size(self):
        return self.fontSize
    
    def get_color(self):
        return self.color


    