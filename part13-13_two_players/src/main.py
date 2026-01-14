# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
robot2 = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

effective_width = 640 - width
effective_height = 480 - height

robot_half_x = width // 2
robot_half_y = height // 2

screen_midpoint_x = 320
screen_midpoint_y = 240

x = screen_midpoint_x + robot_half_x + width
y = screen_midpoint_y - robot_half_y 

x2 = screen_midpoint_x - robot_half_x - width
y2 = screen_midpoint_y - robot_half_y

to_up = False
to_down = False
to_right = False
to_left = False

to_up_2 = False
to_down_2 = False
to_right_2 = False
to_left_2 = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_LEFT:
                to_left = True

            if event.key == pygame.K_w:
                to_up_2 = True
            if event.key == pygame.K_s:
                to_down_2 = True
            if event.key == pygame.K_d:
                to_right_2 = True
            if event.key == pygame.K_a:
                to_left_2 = True

        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_LEFT:
                to_left = False

            if event.key == pygame.K_w:
                to_up_2 = False
            if event.key == pygame.K_s:
                to_down_2 = False
            if event.key == pygame.K_d:
                to_right_2 = False
            if event.key == pygame.K_a:
                to_left_2 = False

        if event.type == pygame.QUIT:
            exit()

    if y >= 0 and to_up:
            y -= 2   
    if y < effective_height and to_down:
            y += 2
    if x < effective_width and to_right:
            x += 2
    if x >= 0 and to_left:
            x -= 2

    if y2 >= 0 and to_up_2:
            y2 -= 2   
    if y2 < effective_height and to_down_2:
            y2 += 2
    if x2 < effective_width and to_right_2:
            x2 += 2
    if x2 >= 0 and to_left_2:
            x2 -= 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    clock.tick(60)