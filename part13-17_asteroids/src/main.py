# WRITE YOUR SOLUTION HERE:

import pygame
from random import randint

pygame.init()
vw = 640
vh = 480
display = pygame.display.set_mode((vw, vh))
clock = pygame.time.Clock()

title = "Asteroids by Gary X."
pygame.display.set_caption(title)

game_font = pygame.font.SysFont("Arial", 24)
title_font = pygame.font.SysFont("Arial", 36)

screen_midpoint_x = vw / 2
screen_midpoint_y = vh / 2

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

rock = pygame.image.load("rock.png")
rock_width = rock.get_width()
rock_height = rock.get_height()

# Robots
x = screen_midpoint_x - robot_width/2
y = vh - robot_height

to_right = False
to_left = False

# Rocks
all_rocks = []
timer = 0
velocity = 2
spawn_delay = 60

# Game State trackers
points = 0
game_over = False
game_started = False

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_started:
            game_started = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_LEFT:
                to_left = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_LEFT:
                to_left = False

    display.fill((0, 0, 0))

    if not game_started:

            title_text = title_font.render("ASTEROIDS by G.X.", True, (255, 110, 199))
            start_text = title_font.render("Click to Start", True, (152, 255, 152))
            
            display.blit(title_text, (screen_midpoint_x - title_text.get_width()/2, screen_midpoint_y - 40))
            display.blit(start_text, (screen_midpoint_x - start_text.get_width()/2, screen_midpoint_y + 20))

    else:

        if not game_over:

            # Robot movement
            if x < vw - robot_width and to_right:
                    x += 9
            if x > 0 and to_left:
                    x -= 9

            # Asteroid generation
            timer += 1
            
            if timer >= spawn_delay:
                a = randint(0, vw - rock_width)
                b = -rock_height
                velocity = randint(1,4)

                all_rocks.append([a, b, velocity])
                
                timer = 0
                spawn_delay = randint(30, 90)

            for this_rock in all_rocks[:]:
                this_speed = this_rock[2] 
                this_rock[1] += this_speed

                this_a = this_rock[0]
                this_b = this_rock[1]

                if this_b + rock_height > vh:
                    game_over = True

                x_collide = (this_a > x) and (this_a < x + robot_width)
                y_collide = (this_b + rock_height > y)

                if x_collide and y_collide: 
                    points += 1
                    all_rocks.remove(this_rock)
                else: 
                    display.blit(rock, (this_rock[0], this_rock[1]))

            # Render logic
            points_text = game_font.render(f"Points: {points}", True, (0, 255, 255))
            display.blit(points_text, (vw * 0.75, vh * 0.05))
            display.blit(robot, (x, y))

        else: 

            game_over_text = title_font.render("GAME OVER", True, (255, 0, 255))
            points_text = title_font.render(f"Final Score: {points}", True, (0, 255, 255))

            display.blit(game_over_text, (screen_midpoint_x - game_over_text.get_width()/2, screen_midpoint_y - 20))
            display.blit(points_text, (screen_midpoint_x - points_text.get_width()/2, screen_midpoint_y + 20))
    
    pygame.display.flip()
    clock.tick(60)
