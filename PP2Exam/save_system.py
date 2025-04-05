import json
import pygame

def save_game(filename, game):
    data = {
        "snake": game.snake.body,
        "direction": game.snake.direction,
        "score": game.level.score,
        "level": game.level.level,
        "speed": game.level.speed,
        "food": {
            "position": game.food.position,
            "weight": game.food.weight,
            "spawn_time": pygame.time.get_ticks()  # Reset timer on load
        }
    }
    with open(filename, "w") as f:
        json.dump(data, f)

def load_game(filename, game):
    with open(filename, "r") as f:
        data = json.load(f)

    game.snake.body = [tuple(pos) for pos in data["snake"]]
    game.snake.direction = tuple(data["direction"])
    game.level.score = data["score"]
    game.level.level = data["level"]
    game.level.speed = data["speed"]
    game.food.position = tuple(data["food"]["position"])
    game.food.weight = data["food"]["weight"]
    game.food.spawn_time = pygame.time.get_ticks()  # New reference point
