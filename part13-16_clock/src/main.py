# WRITE YOUR SOLUTION HERE:

import pygame
import math
from datetime import datetime

pygame.init()

vw = 640
vh = 480
display = pygame.display.set_mode((vw, vh))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    display.fill((0, 0, 0))

    # https://www.pygame.org/docs/ref/draw.html?highlight=circle#pygame.draw.circle
    # circle(surface, color, center, radius, width(optional))
    pygame.draw.circle(display, (255, 0, 0), (vw/2, vh/2), min(vw/2*0.9, vh/2*0.9), 6)
    pygame.draw.circle(display, (255, 0, 0), (vw/2, vh/2), 8)

    now = datetime.now()
    h = now.hour % 12
    m = now.minute
    s = now.second

    title = f"{h:02d}:{m:02d}:{s:02d}"
    pygame.display.set_caption(title)

    h_angle = math.radians(h * 30 - 90)
    s_angle = math.radians(s * 6 - 90)
    m_angle = math.radians(m * 6 - 90)
    
    h_x = vw/2 + math.cos(h_angle) * 100
    h_y = vh/2 + math.sin(h_angle) * 100
    
    m_x = vw/2 + math.cos(m_angle) * 150
    m_y = vh/2 + math.sin(m_angle) * 150

    s_x = vw/2 + math.cos(s_angle) * 180
    s_y = vh/2 + math.sin(s_angle) * 180

    pygame.draw.line(display, (0, 0, 255), (vw/2, vh/2), (h_x, h_y), 8) 
    pygame.draw.line(display, (0, 0, 255), (vw/2, vh/2), (m_x, m_y), 4) 
    pygame.draw.line(display, (0, 0, 255), (vw/2, vh/2), (s_x, s_y), 2) 

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
