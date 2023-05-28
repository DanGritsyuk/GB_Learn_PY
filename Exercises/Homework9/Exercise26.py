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
        unique, counts = np.unique(lstNums, return_counts=True)
        lstUnique = []

        for i, count in enumerate(counts):
            if count == 1:
                lstUnique.append(unique[i])

        print(f'Элементы: {lstNums}' )
        
        uniqueCount = len(lstUnique)
        if uniqueCount > 0:
            print(f'Уникальные элементы: {lstUnique}' )
            print(f'Количество уникальных элементов: {uniqueCount}' )
        else:
            print('Нет уникальных элементов' )