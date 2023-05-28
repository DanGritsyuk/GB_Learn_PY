# Задача 1. Дан список элементов. Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.

import random
import numpy as np
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise26(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        lstNums = [random.randint(0, 10) for _ in range(10)]
        unique = np.unique(lstNums)
        print(f'Элементы: {lstNums}' )
        print(f'Уникальные элементы: {unique}' )
        print(f'Количество уникальных элементов: {len(unique)}' )