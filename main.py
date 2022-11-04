# This is the main file!
from classes.player import player
from classes.scoreBoard import scoreBoard

from classes.director import Director

from services.keyboard_service import KeyboardService
from services.video_service import VideoService

from shared.color import Color
from shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
WHITE = Color(255, 255, 255)



def main():
    

    # create the score banner
    banner = scoreBoard()
    banner.set_text("Score: ")
    
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y - 30)
    position = Point(x, y)

    robot = player()
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    
    
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService('Greed', MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(robot, banner)


if __name__ == "__main__":
    main()