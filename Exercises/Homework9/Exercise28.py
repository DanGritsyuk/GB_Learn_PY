# Задача 3. Создайте двумерный массив случайного размера. Найдите индексы максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива.

import numpy as np
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise28(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        size = (np.random.randint(2, 11), np.random.randint(2, 11))
        numbers = np.random.randint(0, 11, size)
        print(numbers, end='\n\n')

        maxIndex = np.unravel_index(np.argmax(numbers), numbers.shape)
        minIndex = np.unravel_index(np.argmin(numbers), numbers.shape)
        diagonal = np.diag(numbers)

        print(f'Индекс максимального элемента: {maxIndex}')
        print(f'Индекс минимального элемента: {minIndex}')        
        print(f'Элементы главной диагонали: {diagonal}')