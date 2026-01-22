# Complete your game here

# The initial idea for my game, "Monsters Inc": 

# Game Mechanics & Design: 
#   - goal is to accumulate points and avoid monsters
#   - game gets progressively harder over time
#   - coins and monsters are class objects with individual state
#   - TBD if game-board is squares, or free-float coordinates
#   - player uses arrow keys to move robot
#   - collisions trigger state changes

# Coins:
#   - spawn coins at random locations
#   - coins last for random intervals between 3-6 seconds

# Monsters:
#   - monsters roam around the map like zombies
#   - as the game progresses so do the speed and number of them

# Robot: 
#   - this represents the player
#   - collide with coins to earn points 
#   - collide with monster and find out :) 

# Door: 
#   - the door is a gateway/portal 
#   - colliding with it triggers one of 2 events 
#   - event 1 is a coin shower
#   - event 2 is five additional monsters


import pygame

class MonstersInc:

    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Monsters INC.")
        self.window = pygame.display.set_mode((1080, 720))
        self.clock = pygame.time.Clock()

        self.game_font = pygame.font.SysFont("Arial", 24)
        self.title_font = pygame.font.SysFont("Arial", 36)

        self.robot = pygame.image.load("robot.png")
        self.robot_width = robot.get_width()
        self.robot_height = robot.get_height()

        self.game_loop()

    def game_loop(self):
        self.check_events()
        self.paint_screen()

    def check_events(self):
        pass

    def paint_screen(self):
        pass

    def spawn_coin():
        pass

    def spawn_monster():
        pass


class Coin:

    def __init__(self):
        self.__x_coord = 0
        self.__y_coord = 0
        self.__duration = 3

    @property
    def x_coord(self):
        return self.__x_coord

    @x_coord.setter
    def x_coord(self, new_val):
        self.__x_coord = new_val

    @property
    def y_coord(self):
        return self.__y_coord

    @y_coord.setter
    def y_coord(self, new_val):
        self.__y_coord = new_val

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, new_val):
        self.__duration = new_val

