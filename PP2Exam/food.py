import random
import pygame
from config import WIDTH, HEIGHT, GRID_SIZE

class Food:
    def __init__(self):
        self.position = None
        self.weight = None
        self.spawn_time = None

    def generate(self, snake_body):
        while True:
            pos = (
                random.randrange(0, WIDTH, GRID_SIZE),
                random.randrange(0, HEIGHT, GRID_SIZE)
            )
            if pos not in snake_body:
                self.position = pos
                self.weight = random.choice([1, 2, 3])
                self.spawn_time = pygame.time.get_ticks()
                break

    def is_expired(self):
        return pygame.time.get_ticks() - self.spawn_time > 5000