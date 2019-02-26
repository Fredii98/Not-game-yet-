import pygame
from pygame.sprite import Sprite


class Tree(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load('images/tree.bmp')
        self.rect = self.image.get_rect()


