import pygame
from pygame.locals import *
from pathlib import Path

image_path =  Path("Source/mario.png")


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Basic Pygame program')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255,255,255))

    """
    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (250, 250, 250))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)
    """

    image = pygame.image.load('Source\python.png')
    screen.blit(image, (0, 0))

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(image, (0, 0))
        pygame.display.flip()


if __name__ == '__main__': main()
