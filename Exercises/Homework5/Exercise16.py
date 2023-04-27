# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
import random
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise16(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        numbers = [random.randint(1, 10) for i in range(10)]
        print(f'Исходный список: {numbers}')
        print(f'Значения больше 5: {list(filter(lambda x: x > 5, numbers))}')
