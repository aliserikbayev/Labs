import pygame
from config import WIDTH, HEIGHT
from game import Game
from renderer import draw
from events import handle_events
from save_system import save_game, load_game

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    game = Game()

    while game.running:
        handle_events(game)
        game.update()
        draw(screen, game)
        clock.tick(game.level.speed)

    pygame.quit()

if __name__ == "__main__":
    main()
