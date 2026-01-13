# WRITE YOUR SOLUTION HERE:


import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

clock = pygame.time.Clock()

x1 = 0
y1 = height

x2 = 0
y2 = height * 2

velocity1 = 1
velocity2 = 2

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0,0,0))
    window.blit(robot, (x1,y1))
    window.blit(robot, (x2,y2))
    pygame.display.flip()

    if velocity1 > 0 and x1 + width > 640:
        velocity1 = -velocity1
    if velocity1 < 0 and x1 <= 0: 
        velocity1 = -velocity1

    if velocity2 > 0 and x2 + width > 640:
        velocity2 = -velocity2
    if velocity2 < 0 and x2 <= 0: 
        velocity2 = -velocity2

    x1 += velocity1
    x2 += velocity2

    clock.tick(60)
