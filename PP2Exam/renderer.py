import pygame
from config import SNAKE_COLOR, FOOD_COLORS, GRID_SIZE, BG_COLOR


def draw(screen, game):
    screen.fill(BG_COLOR)

    # Draw snake
    for segment in game.snake.body:
        pygame.draw.rect(screen, SNAKE_COLOR, (*segment, GRID_SIZE, GRID_SIZE))

    # Draw food
    pygame.draw.rect(screen, FOOD_COLORS[game.food.weight], (*game.food.position, GRID_SIZE, GRID_SIZE))

    # Draw text
    font = pygame.font.Font(None, 24)
    text = font.render(f"Score: {game.level.score}  Level: {game.level.level}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # draw walls
    for pos in game.wall.positions:
        pygame.draw.rect(screen, (169, 169, 169), (*pos, GRID_SIZE, GRID_SIZE))


    pygame.display.flip()
