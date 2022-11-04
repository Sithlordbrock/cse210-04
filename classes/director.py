# this is the director class!
from classes.gem import Gem
from classes.rock import Rock
import random
from shared.point import Point
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """
    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service

        self.itemsOnScreen = []
        
    def start_game(self, player, scoreBoard):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():

            self._fall_items()

            self._get_inputs(player)
            self._do_updates(player, scoreBoard)
            self._do_outputs(player, scoreBoard)
        self._video_service.close_window()

    def _fall_items(self):
        #items will continually fall from screen
        gem = Gem()
        rock = Rock()
        itemsList = [gem, rock, gem, rock, gem, rock, gem, rock, gem, rock, gem, rock]
        random.shuffle(itemsList)

        for i in range(0,3):
            item = itemsList[i]

            # adds item to screen and keeps track of it
            self.itemsOnScreen.append(item)
            item.set_position(Point(random.randint(1, 60) * 15, 15))
        

    def _get_inputs(self, player):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)        

    def _do_updates(self, player, scoreBoard):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        items = self.itemsOnScreen
      
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        
        for item in items:
            current_y = item.get_position().get_y()
            item.get_position().set_y(current_y + 15)
            if player.get_position().equals(item.get_position()):
                #if robot is at position rock or gem:
                 # change the point value!
                scoreBoard.setScore(item.getPointValue())
        
    def _do_outputs(self, player, scoreBoard):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        items = self.itemsOnScreen
        self._video_service.draw_scoreBoard(scoreBoard)
        self._video_service.draw_item(player)
        self._video_service.draw_items(items)
        self._video_service.flush_buffer()