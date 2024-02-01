#Importing all the modules and libraries 
import os
import pygame


# Initialize Pygame Environment
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (200, 200)
pygame.init()
window = pygame.display.set_mode((900, 500))
winWidth = 900
pygame.display.set_caption('Knights of the Citadel')