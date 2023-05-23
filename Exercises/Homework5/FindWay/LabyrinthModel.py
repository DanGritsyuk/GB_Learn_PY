import random


class LabyrinthModel:
    def __init__(self, x: int, y: int):
        self.data = [[random.randint(0, 1) for j in range(y)] for i in range(x)]
        self.data[0][0] = 1
        self.data[4][4] = 1