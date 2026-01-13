# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))

width = robot.get_width()
height = robot.get_height()

start_x = width
start_y = height

offset_x = 8
offset_y = 24

for y in range(10):
    for x in range(10):
        window.blit(robot, (start_x, start_y))
        start_x += width
    start_x = width + offset_x
    offset_x += 8
    start_y += offset_y

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()