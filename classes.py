from graphics import *
import random
import math
import time

class Runner:
    """Template to the Runner"""

    def __init__(self, x, y, size, window, direction="N"):
        """Constructor for Runner Objects"""
        self.x = x
        self.y = y
        self.size = size
        self.window = window
        self.direction = direction
        self.circle = Circle(Point(x, y), (size * .5))
        self.circle.setFill("green")
        self.hidden = False
        self.circle.draw(self.window)

    def update(self):
        """Un-draws, Moves, then Re-draws the Runner."""
        self.circle.undraw()

        # Check for a new direction
        keys = self.window.checkKeys()
        if "Left" in keys:
            self.direction = "W"
        if "Right" in keys:
            self.direction = "E"
        if "Up" in keys:
            self.direction = "N"
        if "Down" in keys:
            self.direction = "S"

        # Move based on current direction
        if self.direction == "W" and self.x >= (1.5 * self.size):
            self.circle.move(-self.size, 0)
            self.x -= self.size
        if self.direction == "E" and self.x <= (1399 - (1.5 * self.size)):
            self.circle.move(self.size, 0)
            self.x += self.size
        if self.direction == "N" and self.y >= 55:
            self.circle.move(0, -self.size)
            self.y -= self.size
        if self.direction == "S" and self.y <= 625:
            self.circle.move(0, self.size)
            self.y += self.size

        self.circle.draw(self.window)
        self.direction = None

    def getSize(self):
        """Returns the size of the runner"""
        return self.size

    def getX(self):
        """Returns the x value of the upper, left-hand point."""
        return self.x

    def getY(self):
        """Returns the y value of the upper, left-hand point."""
        return self.y

    def setX(self, xCoordinate):
        """Sets the player location to a coordinate"""
        self.x = xCoordinate
        return 0

    def setY(self, yCoordinate):
        """Sets the player location to a coordinate"""
        self.y = yCoordinate
        return 0

    def getDistanceToMines(self, listX, listY, mineCount):
        """Return the distance of the runner to the closest mine (using all mine coordinates)"""
        closest = 2000
        for i in range(mineCount):
            value = math.sqrt(((listX[i] - self.x) ** 2) + ((listY[i] - self.y) ** 2))
            if value < closest:
                closest = value
        return closest

    def getDistanceToObjects(self, listX, listY, obstacleNum):
        """Returns the distance of the runner to the closest object"""
        closest = 2000
        for i in range(obstacleNum):
            value = math.sqrt(((listX[i] - self.x) ** 2) + ((listY[i] - self.y) ** 2))
            if value < closest:
                closest = value
        return closest

    def setColor(self, color):
        """Updates the color of the Runner"""
        self.circle.setFill(color)

    def hidePlayer(self):
        """Undraws the player"""
        self.circle.undraw()

    def draw(self):
        """Draws the player"""
        self.circle.draw(self.window)


class Chaser:
    """Template for creating the Chaser"""

    def __init__(self, x, y, size, window, direction="N"):
        """Constructor for creating Chaser Objects"""
        self.x = x
        self.y = y
        self.size = size
        self.window = window
        self.direction = direction
        self.circle = Circle(Point(x, y), 20)
        self.circle.setFill("blue")

    def update(self, movementNum):
        """Un-draws, Moves, then Re-draws the Chaser."""
        self.circle.undraw()

        # Check for a new direction
        if movementNum == 0:
            self.direction = "X"
        if movementNum == 1:
            self.direction = "W"
        if movementNum == 2:
            self.direction = "E"
        if movementNum == 3:
            self.direction = "N"
        if movementNum == 4:
            self.direction = "S"

        # Move based on current direction
        if self.direction == "W":
            self.circle.move(-self.size, 0)
            self.x -= self.size
        if self.direction == "E":
            self.circle.move(self.size, 0)
            self.x += self.size
        if self.direction == "N":
            self.circle.move(0, -self.size)
            self.y -= self.size
        if self.direction == "S":
            self.circle.move(0, self.size)
            self.y += self.size
        if self.direction == "X":
            self.circle.move(0, 0)

        self.circle.draw(self.window)

    def getX(self):
        """Returns the x value of the upper, left-hand point."""
        return self.x

    def getY(self):
        """Returns the y value of the upper, left-hand point."""
        return self.y

    def setX(self, xCoordinate):
        """Sets the player location to a coordinate"""
        self.x = xCoordinate
        return 0

    def setY(self, yCoordinate):
        """Sets the player location to a coordinate"""
        self.y = yCoordinate
        return 0

    def setColor(self, color):
        """Updates the color of the Runner"""
        self.circle.setFill(color)

    def movementToPlayer(self, playerX, playerY):
        """Returns the best movement for chaser to catch player"""
        closest = 2000
        movementNum = 0
        distanceDown = math.sqrt(((playerX - self.x) ** 2) + ((playerY - (self.y + self.size)) ** 2))
        if distanceDown < closest:
            movementNum = 4
            closest = distanceDown
        distanceUp = math.sqrt(((playerX - self.x) ** 2) + ((playerY - (self.y - self.size)) ** 2))
        if distanceUp < closest:
            movementNum = 3
            closest = distanceUp
        distanceLeft = math.sqrt(((playerX - (self.x - self.size)) ** 2) + ((playerY - self.y) ** 2))
        if distanceLeft < closest:
            movementNum = 1
            closest = distanceLeft
        distanceRight = math.sqrt(((playerX - (self.x + self.size)) ** 2) + ((playerY - self.y) ** 2))
        if distanceRight < closest:
            movementNum = 2
        return movementNum

    def distanceToPlayer(self, playerX, playerY):
        """Returns the distance from chaser to player"""
        closest = 2000
        distanceDown = math.sqrt(((playerX - self.x) ** 2) + ((playerY - (self.y + self.size)) ** 2))
        if distanceDown < closest:
            closest = distanceDown
        distanceUp = math.sqrt(((playerX - self.x) ** 2) + ((playerY - (self.y - self.size)) ** 2))
        if distanceUp < closest:
            closest = distanceUp
        distanceLeft = math.sqrt(((playerX - (self.x - self.size)) ** 2) + ((playerY - self.y) ** 2))
        if distanceLeft < closest:
            closest = distanceLeft
        distanceRight = math.sqrt(((playerX - (self.x + self.size)) ** 2) + ((playerY - self.y) ** 2))
        if distanceRight < closest:
            closest = distanceRight
        return closest
    
    def hideChaser(self):
        """Undraws the chaser"""
        self.circle.undraw()

    def draw(self):
        """Draws the chaser"""
        self.circle.draw(self.window)


class Obstacle:
    """Template for the Obstacles"""

    def __init__(self, x, y, size, window):
        """Constructor for Obstacle Objects"""
        self.x = x
        self.y = y
        self.size = size
        self.window = window

    @staticmethod
    def is_overlapping(x1, y1, x2, y2, size, buffer=100):
        """Check if two obstacles overlap."""
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance < (size + buffer)


class Bush(Obstacle):
    """Template for the Bushes"""

    def __init__(self, x, y, size, window):
        super().__init__(x, y, size, window)
        self.window = window
        self.circle = Circle(Point(x, y), size)
        self.circle.setFill("lime")
        self.circle.draw(self.window)


class Rock(Obstacle):
    """Template for the Rocks"""

    def __init__(self, x, y, size, window):
        super().__init__(x, y, size, window)
        self.window = window
        self.circle = Circle(Point(x, y), size)
        self.circle.setFill("grey")
        self.circle.draw(self.window)

    def setColor(self, color):
        self.circle.setFill(color)


class Mine:
    """Template for creating Mines"""

    def __init__(self, x, y, size, window):
        """Constructor for Mine Objects"""
        self.x = x
        self.y = y
        self.size = size
        self.window = window
        self.circle = Circle(Point(x, y), 20)
        self.circle.setFill("black")
        self.circle.draw(self.window)

    def setColor(self, color):
        self.circle.setFill(color)

    @staticmethod
    def is_overlapping(x1, y1, x2, y2, size):
        """Check if two mines overlap."""
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance < size



class Window:
    def __init__(self):
        self.window = GraphWin("Mine Runner 2.0", 1360, 700, autoflush=False)
        self.window.setBackground("black")
        self.buttons = []

    def display_menu(self):
        self.clear_window()
        self.buttons.clear()  # Clear the previous buttons
        
        # Display title with different colors and appropriate positioning
        title_mine = Text(Point(350, 200), "Mine")
        title_mine.setSize(100)
        title_mine.setFill("green")
        title_mine.draw(self.window)
        
        title_runner = Text(Point(750, 200), "Runner")
        title_runner.setSize(100)
        title_runner.setFill("yellow")
        title_runner.draw(self.window)
        
        title_v2 = Text(Point(1075, 200), "v2")
        title_v2.setSize(100)
        title_v2.setFill("red")
        title_v2.draw(self.window)
        
        # Play button
        play_button = self.create_button(700, 400, "green", "black", "triangle")
        self.buttons.append(play_button)
        
        # Instructions button
        instructions_button = self.create_button(900, 400, "yellow", "black", "dots")
        self.buttons.append(instructions_button)
        
        # Exit button
        exit_button = self.create_button(500, 400, "red", "black", "x")
        self.buttons.append(exit_button)
        
        self.window.update()
        
        return self.get_click()

    def display_instructions(self):
        self.clear_window()
        self.buttons.clear()  # Clear the previous buttons

        # Display instructions title
        title = Text(Point(200, 100), "Instructions")
        title.setSize(36)
        title.setFill("white")
        title.draw(self.window)

        # Display instructions text area
        instructions_text = Text(Point(680, 300), "Use the arrow keys to move the runner.\nAvoid the mines and the chaser.\nCross the red line to clear the level.\nAfter each level, more mines will be added.\nComplete 10 levels to win!\n\nGood luck!")
        instructions_text.setSize(20)
        instructions_text.setFill("white")
        instructions_text.draw(self.window)

        # Back to menu button
        back_button = self.create_square_button(680, 600, "grey", "Menu")
        self.buttons.append(back_button)  # Add back button to buttons list
        self.window.update()

        return back_button

    def create_button(self, x, y, color, icon_color, icon_shape, text=""):
        button = Circle(Point(x, y), 50)
        button.setFill(color)
        button.draw(self.window)
        
        if icon_shape == "triangle":
            icon = Polygon(Point(x-20, y-20), Point(x-20, y+25), Point(x+30, y))
            icon.setFill(icon_color)
            icon.draw(self.window)
        elif icon_shape == "dots":
            self.create_dots(x, y)
        elif icon_shape == "x":
            icon = Text(Point(x, y), "X")
            icon.setSize(36)
            icon.setFill(icon_color)
            icon.draw(self.window)
        
        return button

    def create_square_button(self, x, y, color, text):
        button = Rectangle(Point(x-100, y-30), Point(x+100, y+30))
        button.setFill(color)
        button.draw(self.window)
        
        label = Text(Point(x, y), text)
        label.setSize(16)
        label.setFill("white")
        label.draw(self.window)
        
        return button

    def create_dots(self, x, y):
        dot1 = Circle(Point(x-15, y), 5)
        dot2 = Circle(Point(x, y), 5)
        dot3 = Circle(Point(x+15, y), 5)
        
        for dot in [dot1, dot2, dot3]:
            dot.setFill("black")
            dot.draw(self.window)

    def get_click(self):
        while True:
            click = self.window.getMouse()
            for button in self.buttons:
                if self.is_inside(click, button):
                    return button

    def is_inside(self, point, shape):
        if isinstance(shape, Circle):
            dx = point.getX() - shape.getCenter().getX()
            dy = point.getY() - shape.getCenter().getY()
            return dx * dx + dy * dy <= shape.getRadius() * shape.getRadius()
        elif isinstance(shape, Rectangle):
            return (shape.getP1().getX() <= point.getX() <= shape.getP2().getX() and
                    shape.getP1().getY() <= point.getY() <= shape.getP2().getY())
        return False

    def clear_window(self):
        for item in self.window.items[:]:
            item.undraw()
        self.window.update()

    def build_map(self, level):
        """Builds the map for the game."""
        self.clear_window()

        # Increase mines based on level
        if level == 1:
            increase_mines = 0
        else:
            increase_mines = int(level)

        # Keep track of mines
        mine_list_x = []
        mine_list_y = []
        mine_num = 10 + increase_mines
        mine_size = 40

        # Draw mines on the map
        for _ in range(mine_num):
            while True:
                mine_x = random.randrange(40, 1310)
                mine_y = random.randrange(100, 450)
                overlap = False
                for mx, my in zip(mine_list_x, mine_list_y):
                    if Mine.is_overlapping(mine_x, mine_y, mx, my, mine_size):
                        overlap = True
                        break
                if not overlap:
                    break
            Mine(mine_x, mine_y, mine_size, self.window)
            mine_list_x.append(mine_x)
            mine_list_y.append(mine_y)

        # Keep track of obstacles (trees and rocks)
        obstacle_list_x = []
        obstacle_list_y = []
        obstacle_size = 30
        obstacle_num = 6

        # Draw obstacles on the map
        for _ in range(obstacle_num):
            while True:
                obstacle_x = random.randrange(100, 1310)
                obstacle_y = random.randrange(100, 450)
                overlap = False
                for ox, oy in zip(obstacle_list_x, obstacle_list_y):
                    if Obstacle.is_overlapping(obstacle_x, obstacle_y, ox, oy, obstacle_size):
                        overlap = True
                        break
                if not overlap:
                    break

            rand_obstacle = random.randrange(1, 3)
            if rand_obstacle == 1:
                Rock(obstacle_x, obstacle_y, obstacle_size, self.window)
            else:
                Bush(obstacle_x, obstacle_y, obstacle_size, self.window)
                
            obstacle_list_x.append(obstacle_x)
            obstacle_list_y.append(obstacle_y)

        # Draw chaser spawn line
        line_x3 = 0
        line_x4 = 1500
        line_y3 = 600
        line_y4 = 600
        spawn_line = Line(Point(line_x3, line_y3), Point(line_x4, line_y4))
        spawn_line.setWidth(2)
        spawn_line.setFill("yellow")
        spawn_line.draw(self.window)

        # Create Clear condition
        line_x1 = 0
        line_x2 = 1500
        line_y1 = 50
        line_y2 = 50
        clear_line = Line(Point(line_x1, line_y1), Point(line_x2, line_y2))
        clear_line.setWidth(2)
        clear_line.setFill("red")
        clear_line.draw(self.window)

        return mine_list_x, mine_list_y, mine_num, obstacle_list_x, obstacle_list_y, obstacle_num


class Game:
    def __init__(self, window):
        self.level = 1
        self.window_instance = window  # Use the Window instance
        self.window = window.window  # GraphWin instance
        self.level_text = Text(Point(100, 30), f"Level: {self.level}")
        self.level_text.setSize(20)
        self.level_text.setFill("white")
        self.level_text_drawn = False 
        self.player = None
        self.chaser = None

    def next_level(self):
        """Sets the level of the game."""
        self.level += 1

    def reset_level_text(self):
        self.level_text.setText(f"Level: {self.level}")
        if not self.level_text_drawn:
            self.level_text.draw(self.window)
            self.level_text_drawn = True

    def initialize_characters(self, player_x, player_y, chaser_x, chaser_y, player_size, chaser_size):
        self.player = Runner(player_x, player_y, player_size, self.window)
        self.chaser = Chaser(chaser_x, chaser_y, chaser_size, self.window)

    def play(self):
        """Main function that runs the program."""
        self.window_instance.clear_window()
        mine_list_x, mine_list_y, mine_num, obstacle_list_x, obstacle_list_y, obstacle_num = self.window_instance.build_map(self.level)

        # Draw level text
        self.reset_level_text()

        # Game Flags
        chaser_activated = False
        player_win = False
        game_over = False

        # Number of times player crossed spawn line this level
        cross_num = 0

        # Player Spawn Information
        player_x = 700
        player_y = 700
        player_size = 40

        # Chaser Spawn Information
        chaser_x = 700
        chaser_y = 100
        chaser_size = 40
        chaser_spawn_y = 600

        # Chaser Movement Information
        skip_num = 10
        skip_counter = 0

        # Initialize Player and Chaser
        self.initialize_characters(player_x, player_y, chaser_x, chaser_y, player_size, chaser_size)

        # Main game loop
        while not self.window.closed:
            if not game_over:
                self.level_text.setText(f"Level: {self.level}")

            distance = self.player.getDistanceToMines(mine_list_x, mine_list_y, mine_num)

            # Sets player color based on proximity to mine
            if distance < player_size:
                self.player.setColor("orange")
                self.level_text.setFill("red")
                self.level_text.setText("GAME OVER")
                chaser_activated = False
                game_over = True
                self.window.setBackground("white")

            # Sets player color based on proximity to chaser
            elif self.chaser.distanceToPlayer(self.player.getX(), self.player.getY()) == 0:
                self.player.setColor("orange")
                self.level_text.setFill("red")
                self.level_text.setText("GAME OVER")
                chaser_activated = False
                game_over = True
                self.window.setBackground("white")

            # Sets player color based on proximity to mines
            elif distance < (2 * player_size):
                self.player.setColor("red")
            elif distance < (3 * player_size):
                self.player.setColor("yellow")
            else:
                self.player.setColor("green")

            if distance < player_size and not player_win:
                self.window.setBackground("white")

            if self.chaser.distanceToPlayer(self.player.getX(), self.player.getY()) == 0 and not player_win:
                self.window.setBackground("white")

            # Resets player location once it crosses clear_line
            if self.player.getY() < 100:
                self.player.hidePlayer()
                self.next_level()
                chaser_activated = False
                player_win = True
                self.level_text.setText("You Win!")
                self.level_text.undraw()
                self.level_text_drawn = False  # Reset the flag
                mine_list_x, mine_list_y, mine_num, obstacle_list_x, obstacle_list_y, obstacle_num = self.window_instance.build_map(self.level)
                self.initialize_characters(player_x, player_y, chaser_x, chaser_y, player_size, chaser_size)
                self.reset_level_text()
                cross_num = 0
                skip_num += .5
                self.window.setBackground("black")

            if self.player.getY() <= chaser_spawn_y and cross_num == 0:
                chaser_activated = True
                cross_num += 1
                self.chaser.setColor("blue")

            if chaser_activated:
                if skip_counter >= skip_num:
                    skip_counter = 0
                    movement = self.chaser.movementToPlayer(self.player.getX(), self.player.getY())
                else:
                    movement = 0
                if not self.player.hidden:
                    self.chaser.update(movement)
                else:
                    hidden_movement = random.randrange(1, 5)
                    self.chaser.update(hidden_movement)

            self.player.update()

            distance = self.player.getDistanceToObjects(obstacle_list_x, obstacle_list_y, obstacle_num)
            if distance < player_size:
                self.player.hidePlayer()
                self.chaser.hideChaser()
                self.player.hidden = True
            else:
                self.player.hidden = False

            self.window.update()
            time.sleep(.07)
            skip_counter += 1

        # Ensure chaser and player are redrawn after game over
        self.player.draw()
        self.chaser.draw()