import pygame
import os
import random
import time
width,height = 750,600 
window = ((width,height))
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Atlas's Voyage")

def main():
    running = True
    FPS = 60
    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)

        #To check event in the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
main()
