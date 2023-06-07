import random

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

ball = {
    1: (100, 100),
    2: (400, 100),
    3: (700, 100),
    4: (100, 300),
    5: (400, 300),
    6: (700, 300),
    7: (100, 500),
    8: (400, 500),
    9: (700, 500),
}


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill((255, 0, 0))
    pygame.draw.circle(surface=screen, color=(0, 0, 0), center=(100, 100), radius=50)
    pygame.draw.circle(surface=screen, color=(0, 0, 0), center=(400, 100), radius=50)
    pygame.draw.circle(surface=screen, color=(0, 0, 0), center=(700, 100), radius=50)
    pygame.draw.circle(surface=screen, color=(0, 0, 0), center=(100, 300), radius=50)
    pygame.draw.circle(surface=screen, color=(0, 0, 0), center=(400, 300), radius=50)
    pygame.draw.circle(surface=screen, color=(0, 0, 0), center=(700, 300), radius=50)
    pygame.draw.circle(surface=screen, color=(0, 0, 0), center=(100, 500), radius=50)
    pygame.draw.circle(surface=screen, color=(0, 0, 0), center=(400, 500), radius=50)
    pygame.draw.circle(surface=screen, color=(0, 0, 0), center=(700, 500), radius=50)

    pygame.draw.circle(
        surface=screen, color=(0, 0, 255), center=ball[random.randint(1, 9)], radius=50
    )
    pygame.display.update()
