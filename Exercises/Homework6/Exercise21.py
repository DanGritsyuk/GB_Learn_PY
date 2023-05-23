# Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise21(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        print('Задача 1')