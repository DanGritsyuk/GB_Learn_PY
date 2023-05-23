# Задача 2. Создайте декоратор, повторяющий функцию заданное количество раз.
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise25(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        num = input('Введите число N: ')