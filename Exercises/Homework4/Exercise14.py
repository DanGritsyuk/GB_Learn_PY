# Задача 3. Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.
import math
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise14(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        num = float(input('Введите разряд (при помощи дроби 0.1, 0.01 и т.д.): '))
        print(math.pi - math.pi % num)