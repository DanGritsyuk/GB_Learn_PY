# Задача 1. Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise9(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        print()