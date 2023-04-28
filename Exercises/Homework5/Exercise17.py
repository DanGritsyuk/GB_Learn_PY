# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
import random
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise17(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        numbers = [random.randint(1, 10) for i in range(10)]