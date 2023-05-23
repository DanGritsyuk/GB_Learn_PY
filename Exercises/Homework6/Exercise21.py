# Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise21(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        num = input('Введите число N: ')
        print(f'Результат: {int(num) + int(num * 2) + int(num * 3)}')