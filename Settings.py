import pygame

screen = pygame.display.set_mode((880, 520))
WIDTH = screen.get_width()
HEIGHT = screen.get_height()
image = pygame.image.load("Background.png")
scaled_image = pygame.transform.scale(image, (screen.get_width(), screen.get_height()))
Alien_lines = 3
Alien_columns = 10
score = 0
life = 3

