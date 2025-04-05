
from config import WIDTH, HEIGHT
from snake import Snake
from food import Food
from level import Level
from wall import Wall

class Game:
    def __init__(self):
        self.snake = Snake((WIDTH // 2, HEIGHT // 2))
        self.food = Food()
        self.level = Level()
        self.wall = Wall()
        self.running = True

        self.food.generate(self.snake.body)

    def update(self):
        head = self.snake.move()

        # Wall collision
        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            self.running = False
            return
        if head in self.wall.positions:
            self.running = False
            return

        # Self collision
        if self.snake.collides_with_self():
            self.running = False
            return

        # Food collision
        if head == self.food.position:
            self.level.update_score(self.food.weight)
            self.food.generate(self.snake.body)
        else:
            self.snake.remove_tail()

        if self.food.is_expired():
            self.food.generate(self.snake.body)