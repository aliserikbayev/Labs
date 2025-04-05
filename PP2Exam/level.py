class Level:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.speed = 10

    def update_score(self, weight):
        self.score += weight
        if self.score % 3 == 0:
            self.level += 1
            self.speed += 2