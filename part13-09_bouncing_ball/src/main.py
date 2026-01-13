# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")

width = ball.get_width()
height = ball.get_height()

clock = pygame.time.Clock()

x = 100
y = 0

velocity_x = 5
velocity_y = 5

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0,0,0))
    window.blit(ball, (x,y))
    pygame.display.flip()

    if velocity_x > 0 and x + width > 640:
        velocity_x = -velocity_x

    if velocity_y > 0 and y + height > 480:
        velocity_y = -velocity_y

    if velocity_x < 0 and x <= 0: 
        velocity_x = -velocity_x

    if velocity_y < 0 and y <= 0: 
        velocity_y = -velocity_y

    x += velocity_x
    y += velocity_y

    clock.tick(60)
