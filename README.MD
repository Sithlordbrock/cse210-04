CSE-210 - Fall 2022
Team Thursday 8PM
- Brock Ford
- Ashlee Butterfield
- Spencer Christensen
- Zachary Lindstrom
- Sayri Quinchiguango

CLASSES
(1) Director - directs the game
(2) falling_item - an item that falls vertically down the screen
(3) Gem - a falling_item that gains one point per collision
(4) Rock - a falling_item that loses one point per collision
(5) scoreBoard - keeps track of player score
(6) player - the player with a hashtag sign that moves around the screen
(7) Point - tells player and falling_items their position on the board
(8) Color - tells player and falling_items what color they are
(9) KeyboardService - maps keyboard input to player movement
(10) VideoService - prints all outcomes to the screen 

GAME SPECIFICATION:
https://byui-cse.github.io/cse210-course-competency/inheritance/materials/greed-specification.html

OVERVIEW:
Greed is a game in which the player seeks to gather as many falling gems as possible. The game continues as long as the player wants more!

RULES:
Greed is played according to the following rules:
- Gems (*) and rocks (o) randomly appear and fall from the top of the screen.
- The player (#) can move left or right along the bottom of the screen.
- If the player touches a gem they earn a point.
- If the player touches a rock they lose a point.
- Gems and rocks are removed when the player touches them.
- The game continues until the player closes the window.

REQUIREMENTS
Your program must also meet the following requirements.
- The program must have a README file.
- The program must have at least eight classes.
- Each module, class and method must have a corresponding comment.
- The game must remain generally true to the order of play described earlier.

HAVE SOME FUN
Make the game your own by enhancing it any way you like. Here are a few ideas.
- Enhanced gems and rocks (multiple kinds, different points).
- Enhanced player movement (up and down in a limited range)
- Enhanced game play and game over messages.
- Enhanced gem, rock and player representation (colors or better symbols)
