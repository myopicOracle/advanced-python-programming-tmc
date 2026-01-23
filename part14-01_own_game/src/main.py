# Complete your game here

# "Monsters Inc" - Final Project for Advanced Programming with Python: 

# Game Mechanics & Design: 
#   - goal is to accumulate points and avoid monsters
#   - game gets progressively harder over time
#   - coins and monsters are class objects with individual state
#   - player uses arrow keys to move robot
#   - collisions trigger state changes

# Coins:
#   - spawn coins at random locations
#   - spawns happen at random intervals between 1-5 seconds

# Monsters:
#   - monsters roam around the map like zombies, bouncing off walls
#   - monsters spawn in at random interval between 5-20 seconds
#   - each monster is assigned a random velocity when initialized
#   - as the game progresses the speed of all monsters increase 

# Robot: 
#   - this represents the player
#   - collide with coins to earn points 
#   - collide with monster and it's game over 


import pygame
from random import randint

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

        self.screen_midpoint_x = 1080 / 2
        self.screen_midpoint_y = 720 / 2

        self.robot = pygame.image.load("robot.png")
        self.robot_width = self.robot.get_width()
        self.robot_height = self.robot.get_height()

        self.coin = pygame.image.load("coin.png")
        self.coin_width = self.coin.get_width()
        self.coin_height = self.coin.get_height()

        self.monster = pygame.image.load("monster.png")
        self.monster_width = self.monster.get_width()
        self.monster_height = self.monster.get_height()

    def setup_state(self):
        self.all_coins = []
        self.all_monsters = []

        self.robot_velocity = 5
        self.robot_x = self.screen_midpoint_x - (self.robot_width/2)
        self.robot_y = self.screen_midpoint_y - (self.robot_height/2)

        self.to_up = False
        self.to_down = False
        self.to_right = False
        self.to_left = False

        self.coin_timer = 0
        self.coin_spawn_delay = 180

        self.monster_timer = 0
        self.monster_spawn_delay = 600
        
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

            if event.type == pygame.MOUSEBUTTONDOWN and not self.game_started:
                self.game_started = True

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
        self.window.fill((109, 129, 150))

        if not self.game_started:
            title_text = self.title_font.render("MONSTERS INC", True, (255, 110, 199))
            start_text = self.title_font.render("Click to Start", True, (152, 255, 152))
            
            self.window.blit(title_text, (self.screen_midpoint_x - title_text.get_width()/2, self.screen_midpoint_y - 40))
            self.window.blit(start_text, (self.screen_midpoint_x - start_text.get_width()/2, self.screen_midpoint_y + 20))

        else:
            if not self.game_over:
                self.update_player()
                self.spawn_coin()
                self.spawn_monster()

                rules_text = self.game_font.render(f"Collect Coins, avoid Monsters!", True, (0, 255, 255))
                self.window.blit(rules_text, (50, 25))

                points_text = self.game_font.render(f"Points: {self.points}", True, (0, 255, 255))
                self.window.blit(points_text, (1080 - points_text.get_width() - 50, 25))

            else:
                game_over_text = self.title_font.render("GAME OVER", True, (255, 0, 255))
                points_text = self.title_font.render(f"Final Score: {self.points}", True, (0, 255, 255))

                self.window.blit(game_over_text, (self.screen_midpoint_x - game_over_text.get_width()/2, self.screen_midpoint_y - 20))
                self.window.blit(points_text, (self.screen_midpoint_x - points_text.get_width()/2, self.screen_midpoint_y + 20))

    def update_player(self):
        if self.robot_y > 0 and self.to_up:
                self.robot_y -= self.robot_velocity
        if self.robot_y < 720 - self.robot_height and self.to_down:
                self.robot_y += self.robot_velocity
        if self.robot_x < 1080 - self.robot_width and self.to_right:
                self.robot_x += self.robot_velocity
        if self.robot_x > 0 and self.to_left:
                self.robot_x -= self.robot_velocity

        self.window.blit(self.robot, (self.robot_x, self.robot_y))

    def spawn_coin(self):
        self.coin_timer += 1
        if self.coin_timer >= self.coin_spawn_delay:
            new_coin = Coin()
            new_coin.x_coord = randint(0, 1080 - self.coin_width)
            new_coin.y_coord = randint(0, 720 - self.coin_height)
            self.all_coins.append(new_coin)

            self.coin_timer = 0
            self.coin_spawn_delay = randint(60, 300)

        for this_coin in self.all_coins[:]:
            if self.check_collision(this_coin, self.coin_width, self.coin_height):
                self.points += 1
                self.all_coins.remove(this_coin)
            else:
                self.window.blit(self.coin, (this_coin.x_coord, this_coin.y_coord))

    def spawn_monster(self):
        self.monster_timer += 1
        if self.monster_timer >= self.monster_spawn_delay:
            velocity = randint(1, 4)
            new_monster = Monster(velocity)
            new_monster.x_coord = randint(0, 1080 - self.monster_width)
            new_monster.y_coord = randint(0, 720 - self.monster_height)
            self.all_monsters.append(new_monster)

            self.monster_timer = 0
            self.monster_spawn_delay = randint(300, 1200)

        for this_monster in self.all_monsters[:]:
            if this_monster.x_coord + self.monster_width > 1080 or this_monster.x_coord < 0:
                this_monster.velocity_x = -this_monster.velocity_x
            if this_monster.y_coord + self.monster_height > 720 or this_monster.y_coord < 0:
                this_monster.velocity_y = -this_monster.velocity_y
            
            this_monster.x_coord += this_monster.velocity_x
            this_monster.y_coord += this_monster.velocity_y

            if this_monster.velocity_x < 15:
                this_monster.velocity_x += 0.001
                this_monster.velocity_y += 0.001

            if self.check_collision(this_monster, self.monster_width, self.monster_height):
                self.game_over = True
            else:
                self.window.blit(self.monster, (this_monster.x_coord, this_monster.y_coord))

    def check_collision(self, this_obj, width, height):
        x_collide = (this_obj.x_coord < self.robot_x + self.robot_width and this_obj.x_coord + width > self.robot_x)
        y_collide = (this_obj.y_coord < self.robot_y + self.robot_height and this_obj.y_coord + height > self.robot_y)
        return x_collide and y_collide


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
        self.__velocity_x = velocity
        self.__velocity_y = velocity

    @property
    def velocity_x(self):
        return self.__velocity_x

    @velocity_x.setter
    def velocity_x(self, new_val):
        self.__velocity_x = new_val

    @property
    def velocity_y(self):
        return self.__velocity_y

    @velocity_y.setter
    def velocity_y(self, new_val):
        self.__velocity_y = new_val


# Test
if __name__ == "__main__":
    MonstersInc()
