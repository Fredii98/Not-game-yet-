import pygame
from pygame.sprite import Group

from settings import Settings
from character import Character
import game_function as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.SCREEN_WIDTH, ai_settings.SCREEN_HEIGHT))
    pygame.display.set_caption(ai_settings.TITLE)
    character = Character(screen, ai_settings)
    trees = Group()
    gf.add_tree(trees, screen)
    while True:
        gf.check_events(character, trees)
        character.update()
        gf.update_screen(screen, ai_settings, character, trees)


run_game()
