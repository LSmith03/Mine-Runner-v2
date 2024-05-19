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
        self.circle.setFill("black")
        self.circle.draw(self.window)

    def update(self, movementNum):
        """Un-draws, Moves, then Re-draws the Runner."""
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
        """Undraws the player"""
        self.circle.undraw()


class Menu:

    def __init__(self):
        pass

    def display_menu(self):
        pass

class Game:
    def __init__(self):
        self.level = 1
        self.window = GraphWin("Mine Runner 2.0", 1400, 700, autoflush=False)
        self.window.setBackground("black")
        self.level_text = Text(Point(100, 30), f"Level: {self.level}")
        self.level_text.setSize(20)
        self.level_text.setFill("white")
        self.level_text_drawn = False 

    def clear_window(self):
        """Clears the window of all objects."""
        for item in self.window.items[:]:
            item.undraw()
        self.window.update()

    def build_map(self):
        """Builds the map for the game."""
        self.clear_window()

        # Increase mines based on level
        if self.level == 1:
            increase_mines = 0
        else:
            increase_mines = int(self.level * 1.5)

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

        self.level_text.setText(f"Level: {self.level}")
        if not self.level_text_drawn:
            self.level_text.draw(self.window)
            self.level_text_drawn = True

        return mine_list_x, mine_list_y, mine_num, obstacle_list_x, obstacle_list_y, obstacle_num

    def next_level(self):
        """Sets the level of the game."""
        self.level += 1

    def play(self):
        """Main function that runs the program."""
        mine_list_x, mine_list_y, mine_num, obstacle_list_x, obstacle_list_y, obstacle_num = self.build_map()

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

        # Create Player and Chaser
        player = Runner(player_x, player_y, player_size, self.window)
        chaser = Chaser(chaser_x, chaser_y, chaser_size, self.window)

        # Main game loop
        while not self.window.closed:
            if not game_over:
                self.level_text.setText(f"Level: {self.level}")

            distance = player.getDistanceToMines(mine_list_x, mine_list_y, mine_num)

            # Sets player color based on proximity to mine
            if distance < player_size:
                player.setColor("orange")
                self.level_text.setFill("red")
                self.level_text.setText("GAME OVER")
                chaser_activated = False
                game_over = True
                self.window.setBackground("white")

            # Sets player color based on proximity to chaser
            elif chaser.distanceToPlayer(player.getX(), player.getY()) == 0:
                player.setColor("orange")
                self.level_text.setFill("red")
                self.level_text.setText("GAME OVER")
                chaser_activated = False
                game_over = True
                self.window.setBackground("white")

            # Sets player color based on proximity to mines
            elif distance < (2 * player_size):
                player.setColor("red")
            elif distance < (3 * player_size):
                player.setColor("yellow")
            else:
                player.setColor("green")

            if distance < player_size and not player_win:
                self.window.setBackground("white")

            if chaser.distanceToPlayer(player.getX(), player.getY()) == 0 and not player_win:
                self.window.setBackground("white")

            # Resets player location once it crosses clear_line
            if player.getY() < 100:
                player.hidePlayer()
                self.next_level()
                chaser_activated = False
                player_win = True
                self.level_text.setText("You Win!")
                self.level_text.undraw()
                self.level_text_drawn = False  # Reset the flag
                mine_list_x, mine_list_y, mine_num, obstacle_list_x, obstacle_list_y, obstacle_num = self.build_map()
                player = Runner(player_x, player_y, player_size, self.window)
                chaser = Chaser(chaser_x, chaser_y, chaser_size, self.window)
                cross_num = 0
                skip_num += .5
                self.window.setBackground("black")

            if player.getY() <= chaser_spawn_y and cross_num == 0:
                chaser_activated = True
                cross_num += 1
                chaser.setColor("blue")

            if chaser_activated:
                if skip_counter >= skip_num:
                    skip_counter = 0
                    movement = chaser.movementToPlayer(player.getX(), player.getY())
                else:
                    movement = 0
                if not player.hidden:
                    chaser.update(movement)
                else:
                    hidden_movement = random.randrange(1, 5)
                    chaser.update(hidden_movement)

            player.update()

            distance = player.getDistanceToObjects(obstacle_list_x, obstacle_list_y, obstacle_num)
            if distance < player_size:
                player.hidePlayer()
                # chaser.hideChaser()
                player.hidden = True
            else:
                player.hidden = False

            self.window.update()
            time.sleep(.07)
            skip_counter += 1
