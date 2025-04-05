import pygame
from save_system import *
from config import UP, DOWN, LEFT, RIGHT

def handle_events(game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:  # Save game
                save_game("savefile.json", game)
            elif event.key == pygame.K_l:  # Load game
                load_game("savefile.json", game)
            if event.key == pygame.K_UP:
                game.snake.set_direction(UP)
            elif event.key == pygame.K_DOWN:
                game.snake.set_direction(DOWN)
            elif event.key == pygame.K_LEFT:
                game.snake.set_direction(LEFT)
            elif event.key == pygame.K_RIGHT:
                game.snake.set_direction(RIGHT)