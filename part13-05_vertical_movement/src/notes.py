# # BASIC ANIMATION
# import pygame

# pygame.init()
# window = pygame.display.set_mode((640, 480))

# robot = pygame.image.load("robot.png")

# x = 0
# y = 0
# clock = pygame.time.Clock()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()

#     window.fill((0, 0, 0))
#     window.blit(robot, (x, y))
#     pygame.display.flip()

#     x += 1
#     clock.tick(60)


# BOUNCING OFF WALLS
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    x += velocity
    if velocity > 0 and x+robot.get_width() >= 640:
        velocity = -velocity
    if velocity < 0 and x <= 0:
        velocity = -velocity

    clock.tick(60)


# # ROTATION

# import pygame
# import math

# pygame.init()
# window = pygame.display.set_mode((640, 480))

# robot = pygame.image.load("robot.png")

# angle = 0
# clock = pygame.time.Clock()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()

#     x = 320+math.cos(angle)*100-robot.get_width()/2
#     y = 240+math.sin(angle)*100-robot.get_height()/2

#     window.fill((0, 0, 0))
#     window.blit(robot, (x, y))
#     pygame.display.flip()

#     angle += 0.01
#     clock.tick(60)