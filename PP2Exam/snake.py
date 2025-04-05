from config import GRID_SIZE

class Snake:
    def __init__(self, start_pos):
        self.body = [start_pos]
        self.direction = (1, 0)

    def set_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0] * GRID_SIZE,
                    head_y + self.direction[1] * GRID_SIZE)
        self.body.insert(0, new_head)
        return new_head

    def remove_tail(self):
        self.body.pop()

    def collides_with_self(self):
        return self.body[0] in self.body[1:]

    def get_head(self):
        return self.body[0]