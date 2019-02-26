import sys

import pygame

from tree import Tree


def add_tree(trees, screen):
    tree = Tree(screen)
    tree.rect.y = 100
    tree.rect.x = 100
    trees.add(tree)
    tree = Tree(screen)
    tree.rect.y = 100
    tree.rect.x = 600
    trees.add(tree)
    tree = Tree(screen)
    tree.rect.y = 500
    tree.rect.x = 100
    trees.add(tree)
    tree = Tree(screen)
    tree.rect.y = 500
    tree.rect.x = 600
    trees.add(tree)


def check_keydown_events(event, character):
    if event.key == pygame.K_UP:
        character.moving_up = True
    elif event.key == pygame.K_DOWN:
        character.moving_down = True
    elif event.key == pygame.K_LEFT:
        character.moving_left = True
    elif event.key == pygame.K_RIGHT:
        character.moving_right = True


def check_keyup_events(event, character):
    if event.key == pygame.K_UP:
        character.moving_up = False
    elif event.key == pygame.K_DOWN:
        character.moving_down = False
    elif event.key == pygame.K_LEFT:
        character.moving_left = False
    elif event.key == pygame.K_RIGHT:
        character.moving_right = False


def check_events(character, trees):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, character)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, character)


def update_screen(screen, ai_settings, character, trees):
    screen.fill(ai_settings.SCREEN_COLOR)

    character.blitme()
    trees.draw(screen)
    pygame.display.flip()
