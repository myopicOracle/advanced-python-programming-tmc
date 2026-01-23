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
        self.setup_gui()
        self.setup_state()
        self.game_loop()

    def setup_gui(self):
        pygame.display.set_caption("Monsters INC.")
        self.window = pygame.display.set_mode((1080, 720))
        self.clock = pygame.time.Clock()

        self.game_font = pygame.font.SysFont("Arial", 24)
        self.title_font = pygame.font.SysFont("Arial", 36)

        self.robot = pygame.image.load("robot.png")
        self.coin = pygame.image.load("coin.png")
        self.monster = pygame.image.load("monster.png")

    def setup_state(self):
        self.all_coins = []
        self.all_monsters = []

        self.robot_velocity = 2
        self.robot_x = 0
        self.robot_y = 0

        self.to_up = False
        self.to_down = False
        self.to_right = False
        self.to_left = False

        self.points = 0
        self.game_over = False
        self.game_started = False

    def game_loop(self):
        while True: 
            self.check_events()
            self.paint_screen()
            pygame.display.flip()
            self.clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.to_up = True
                if event.key == pygame.K_DOWN:
                    self.to_down = True
                if event.key == pygame.K_RIGHT:
                    self.to_right = True
                if event.key == pygame.K_LEFT:
                    self.to_left = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.to_up = False
                if event.key == pygame.K_DOWN:
                    self.to_down = False
                if event.key == pygame.K_RIGHT:
                    self.to_right = False
                if event.key == pygame.K_LEFT:
                    self.to_left = False

    def paint_screen(self):
        # Clear previous screen
        self.window.fill((0, 0, 0))

        # Update object coordinates
        if self.robot_y > 0 and self.to_up:
                self.robot_y -= self.robot_velocity
        if self.robot_y < 720 - self.robot.get_height() and self.to_down:
                self.robot_y += self.robot_velocity
        if self.robot_x < 1080 - self.robot.get_width() and self.to_right:
                self.robot_x += self.robot_velocity
        if self.robot_x > 0 and self.to_left:
                self.robot_x -= self.robot_velocity

        # Render new location
        self.window.blit(self.robot, (self.robot_x, self.robot_y))


    def spawn_coin():
        pass

    def spawn_monster():
        pass


class Sprite:

    def __init__(self):
        self.__x_coord = 0
        self.__y_coord = 0

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


class Coin(Sprite):

    def __init__(self, duration = 3):
        super().__init__()
        self.__duration = duration;

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, new_val):
        self.__duration = new_val


class Monster(Sprite):

    def __init__(self, velocity = 1):
        super().__init__()
        self.__velocity = velocity;

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, new_val):
        self.__velocity = new_val


# Test
if __name__ == "__main__":
    MonstersInc()
