# config.py

WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
SNAKE_COLOR = (0, 255, 0)
FOOD_COLORS = {1: (255, 0, 0), 2: (255, 165, 0), 3: (255, 255, 0)}
BG_COLOR = (0, 0, 0)
FOOD_LIFETIME = 5000  # in milliseconds

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)