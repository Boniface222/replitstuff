# Based on on https://repl.it/talk/learn/A-Starter-Guide-to-Pygame/11741

import pygame, time

pygame.init()
width, height = 800,  600
backgroundColor = 255,  0,  0
blanksurface = pygame.Surface((150,100))
dvdLogoRect = blanksurface.get_rect()
dvdLogoSpeed = [1, 1]

screen = pygame.display.set_mode((width, height))

while True:
    screen.fill(backgroundColor)
    screen.blit(blanksurface, dvdLogoRect)
    dvdLogoRect = dvdLogoRect.move(dvdLogoSpeed)
    if dvdLogoRect.left < 0 or dvdLogoRect.right > width:
        dvdLogoSpeed[0] = -dvdLogoSpeed[0]
    if dvdLogoRect.top < 0 or dvdLogoRect.bottom > height:
        dvdLogoSpeed[1] = -dvdLogoSpeed[1]

    pygame.display.flip()
    time.sleep(10 / 1000)
