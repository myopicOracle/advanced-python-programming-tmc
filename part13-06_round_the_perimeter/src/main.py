# # WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

clock = pygame.time.Clock()

x = 0
y = 0

velocity_x = 1
velocity_y = 0

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0,0,0))
    window.blit(robot, (x,y))
    pygame.display.flip()

    if velocity_x > 0 and velocity_y == 0 and x + width > 640:
        velocity_x = 0
        velocity_y = 1

    if velocity_y > 0 and y + height > 480:
        velocity_x = -1
        velocity_y = 0

    if velocity_x < 0 and x <= 0: 
        velocity_x = 0
        velocity_y = -1

    if velocity_y < 0 and y <= 0: 
        velocity_x = 1
        velocity_y = 0 

    x += velocity_x
    y += velocity_y

    clock.tick(60)
