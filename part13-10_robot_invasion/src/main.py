# WRITE YOUR SOLUTION HERE:

import pygame
from random import randint, randrange, choice

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
clock = pygame.time.Clock()

width = robot.get_width()
height = robot.get_height()

velocity_x = 0
velocity_y = 2

all_robots = []

timer = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    timer += 1
    
    if timer >= 20:
        x = randint(0, 640-width)
        y = -height
        
        all_robots.append([x, y, velocity_x, velocity_y])
        
        timer = 0

    window.fill((0, 0, 0))

    for this_robot in all_robots:
        this_x = this_robot[0]
        this_y = this_robot[1]
        this_vx = this_robot[2]
        this_vy = this_robot[3]

        if this_robot[3] > 0 and this_robot[1] + height >= 480:
            this_robot[3] = 0
            this_robot[2] = choice([-2, 2])

        this_robot[0] += this_robot[2]
        this_robot[1] += this_robot[3]

        window.blit(robot, (this_robot[0], this_robot[1]))

    pygame.display.flip()
    clock.tick(60)