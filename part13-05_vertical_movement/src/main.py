# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

clock = pygame.time.Clock()

x = 0
y = 0

velocity = 1

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0,0,0))
    window.blit(robot, (x,y))
    pygame.display.flip()

    if velocity > 0 and y + height > 480:
        velocity = -velocity
    if velocity < 0 and y <= 0: 
        velocity = -velocity

    y += velocity

    clock.tick(60)
