import random
import threading
import time

import pygame

pygame.init()


# def rat():
#     threading.Timer(1.0, rat).start()
#     pygame.draw.circle(
#         surface=screen,
#         color=(0, 255, 255),
#         center=ball[random.randint(1, 9)],
#         radius=50,
#     )


screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Thief Game ")

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

x, y = 100, 100

counter = 0
sleep = 1
temp = 0


while True:
    time.sleep(sleep)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y += 200
                if y > 500:
                    y = 100
                pygame.display.update()
            elif event.key == pygame.K_UP:
                y -= 200
                if y < 100:
                    y = 500
                pygame.display.update()
            elif event.key == pygame.K_RIGHT:
                x += 300
                if x > 700:
                    x = 100
                pygame.display.update()
            elif event.key == pygame.K_LEFT:
                x -= 300
                if x < 100:
                    x = 700
                pygame.display.update()

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

    pygame.draw.circle(surface=screen, color=(0, 255, 0), center=(x, y), radius=50)
    pygame.draw.circle(
        surface=screen,
        color=(0, 255, 255),
        center=ball[random.randint(1, 9)],
        radius=50,
    )

    # temp += 1
    # if temp > 5000:
    #     pygame.draw.circle(
    #         surface=screen,
    #         color=(0, 255, 255),
    #         center=ball[random.randint(1, 9)],
    #         radius=50,
    #     )
    #     temp = 0

    # print(temp)
    pygame.display.update()
    counter += 1
