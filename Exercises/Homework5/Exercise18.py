# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
import random
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise18(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        numbers = [random.randint(1, 10) for i in range(10)]
        print(f'Исходный список: {numbers}')

        duplicates = {}
        for i in numbers:
            if i in duplicates:
                duplicates[i] += 1
            else:
                duplicates[i] = 1
        setList = list(set(numbers))

        for key in duplicates:
            print(f'{key} - {duplicates[key]}')
        print(setList)